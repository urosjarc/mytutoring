import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class java {
    public static URI url(String path){
        return URI.create("http://localhost:5000/" + path);
    }

    public static ArrayList<HashMap<String, String>> parseResponse(String response){
        ArrayList<HashMap<String, String>> data = new ArrayList<>();
        String[] items = response.substring(1,response.length()-3).replace(",\"", "|").replace("\"", "").split("},");
        for(String item: items){
            String[] vals = item.substring(1).split("\\|");
            HashMap<String, String> dict = new HashMap<>();
            for (String val : vals) {
                String[] ele = val.split(":");
                dict.put(ele[0], ele[1]);
            }
            data.add(dict);
        }
        return data;
    }

    public static Object[] parseInput(String input){
        String[] inputs = input.replace("[", "").replace("]", "").split(",");
        return Arrays.stream(inputs).toList().toArray();
    }

    public static String encodeRequest(ArrayList<HashMap<String, String>> request){
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append('[');
        request.forEach(stringHashMap -> {
            stringBuilder.append('{');
            stringHashMap.forEach((s, string) -> stringBuilder
                    .append('"' + s + '"')
                    .append(": ")
                    .append(string)
                    .append(", "));
            stringBuilder.append("}, ");
        });
        stringBuilder.append(']');
        return stringBuilder.toString();
    }

    public static String request(String path, String data){
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request;
        if(data!=null){
            request = HttpRequest.newBuilder(url(path))
                    .header("content-type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(data))
                    .build();
        } else {
            request = HttpRequest.newBuilder(url(path))
                    .header("content-type", "application/json")
                    .GET().build();
        }

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            return response.body();
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
    public static void printResult(ArrayList<HashMap<String, String>> results){
        System.out.println();
        if(results.size() == 0){
            System.out.println("No tests found");
            return;
        }

        String[] keys = {"pass", "time [sec]", "input", "output", "expected"};
        HashMap<String, Integer> length = new HashMap<>();
        for (String key : keys) length.put(key, 0);

        for(HashMap<String, String> result: results){
            result.put("pass", result.get("pass").equals("true") ? "....": "XXX");
            for (String key : keys) {
                length.put(key, Math.max(Math.max(length.get(key), key.length()), result.get(key).length()));
            }
        }

        for (String key : keys) {
            System.out.print(extend_str(key, length.get(key)) + "    ");
        }
        System.out.println();
        for (HashMap<String, String> result : results) {
            for (String key : keys) {
                System.out.print(extend_str(result.get(key), length.get(key)) + "    ");
            }
            System.out.println();
        }
    }

    private static String extend_str(String key, int length) {
        int diff = length - key.length();
        for (int i = 0; i < diff; i++) {
            key += " ";
        }
        return key;
    }

    public static void test(Class cls){
        String path = "test/" + cls.getName();

        //GETTING METHOD
        Method run = null;
        for(Method method: cls.getDeclaredMethods()){
            if(method.getName().equals("wrapper")){
               run = method;
               break;
            }
        }
        assert run != null;

        //GETTING ARGS FOR EVALUATION
        String response = request(path, null);
        ArrayList<HashMap<String, String>> tests = parseResponse(response);
        for(HashMap<String, String> test: tests){
            try {
                Object[] args = parseInput(test.get("input"));
                long startTime = System.nanoTime();
                Object result = run.invoke(null, args);
                long stopTime = System.nanoTime();
                if(result != null){
                    double duration = (stopTime - startTime)/1.0e9;
                    test.put("time [sec]", Double.toString(duration));
                    test.put("output", result.toString());
                }
            } catch (IllegalAccessException | InvocationTargetException e) {
                throw new RuntimeException(e);
            }
        }

        String data = encodeRequest(tests)
                .replace(", }", "}")
                .replace(", ]", "]");
        String response2 = request(path, data);
        ArrayList<HashMap<String, String>> results = parseResponse(response2);
        printResult(results);
    }
}
