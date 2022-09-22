import json
from typing import Callable
from urllib.request import Request, urlopen


def url(path):
	return f'http://localhost:5000/{path}'


def request(path, data=None):
	post_request = Request(
		url=url(path),
		data=json.dumps(data).encode() if data is not None else None,
		headers={"Content-Type": "application/json; charset=UTF-8"})
	return json.loads(urlopen(post_request).read().decode())


def test(function: Callable):
	path = f'test/{function.__name__}'
	tests = request(path)
	predictions = []
	for i, test in enumerate(tests):
		result = function(*test['input'])
		if result is not None:
			test['output'] = result
			predictions.append(test)
	results = request(path, data=predictions)
	items = results[0].items()
	for ele, val in items:
		print(f'{ele.capitalize():<20}', end='')
	print()
	for result in results:
		for ele, val in items:
			print(f'{str(result[ele]):<20}', end='')
		print()
