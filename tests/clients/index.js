function url(path){
    return `http://localhost:5000/${path}`;
}
function request(path, data=null){
    let options = {};
    if(data != null){
        options = {
            method: "POST",
            body: data
        };
    }
    fetch(url(path), options).then(data=>data.json());
}
function extend_str(obj, length: int){
    let obj = String(obj);
    let diff = length - obj.length;
    return obj + " " * diff;
}
function print_results(results){
    console.log();
    if(results.length == 0){
        return console.log("No tests found");
    }

	let keys = ['pass', 'time [sec]', 'input', 'output', 'expected']
    let length = {};
    for(let key of keys) length[key] = 0;
	for(let result of results){
		result['pass'] = "...." if result['pass'] else "XXX"
		for(let k of keys){
			length[k] = Math.max(length[k], String(k).length, String(result[k]).length))
		}
    }

    table = "<tr>";
	for(let k of keys)
		table += `${k}`;
    table += "</tr><tr>";
	for(let result of results)
		for(let k of keys)
            table += `${result[k]}`;
    table += "</tr>";

    let table = document.getElementById("table");
    table.innerHTMl += table;
}
function test(fun){
    let path = `test/{fun.name}`;
    request(path).then(tests => {
        predictions = [];
        for(let test of tests){
            let start = performance.now();
            fun(*test.input);
            let stop = performance.now();
            if(result != null){
                test.output = result;
                test['time [sec]'] = Math.round((stop-start)*1000, 10);
                predictions.push(test)
            }
        }

        request(path, data=predictions).then(results => {
            print_results(results);
        })
    })
}
