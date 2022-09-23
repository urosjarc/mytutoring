function url(path){
    return `http://localhost:5000/${path}`;
}
function request(path, data=null){
    let options = {};
    if(data != null){
        options = {
            method: "POST",
            body: JSON.stringify(data),
        };
    }
    options.mode = 'cors';
    options.headers = {
        'Content-Type': 'application/json'
    };
    return fetch(url(path), options).then(data=>data.json());
}
function extend_str(obj, length){
    obj = String(obj);
    let diff = length - obj.length;
    return obj + " " * diff;
}
function print_results(results){
    let tableDOM = document.getElementById("table");

    if(results.length == 0){
        return tableDOM.innerHTML = "<h1 style='color: red'>No tests found</h1>";
    }

	let keys = ['pass', 'time [sec]', 'input', 'output', 'expected']
	for(let result of results){
		result['pass'] = result['pass'] ? "<h1 style='color: green'>&#9745;</h1>" : "<h1 style='color: red'>&#9746;<h1>";
    }

    let table = "<tr>";
	for(let k of keys){
		table += `<td><h1>${k}</h1></td>`;
    }
    table += "</tr>";

	for(let result of results){
        table += "<tr>";
		for(let k of keys){
            table += `<td><h2>${result[k]}</h2></td>`;
        }
        table += "</tr>";
    }

    tableDOM.innerHTML = table;
}
function test(fun){
    let path = `test/${fun.name}`;
    request(path).then(tests => {
        predictions = [];
        for(let test of tests){
            let start = performance.now();
            let result = fun(...test.input);
            let stop = performance.now();
            if(result != null){
                test.output = result;
                test['time [sec]'] = ((stop-start)/1000.0).toFixed(5);
                predictions.push(test)
            }
        }

        request(path, data=predictions).then(results => {
            print_results(results);
        })
    })
}
