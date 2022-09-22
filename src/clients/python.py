import json
import time
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


def extend_str(obj, length: int):
	obj = str(obj)
	diff = length - len(obj)
	return obj + " " * diff


def print_results(results):
	print()
	keys = ['pass', 'time [sec]', 'input', 'output', 'expected']
	if len(results) == 0:
		return print("No tests found")

	# Calculating lengths
	length = {k: 0 for k in keys}
	for result in results:
		result['pass'] = "...." if result['pass'] else "XXX"
		for k in keys:
			length[k] = max(length[k], len(str(k)), len(str(result[k])))

	for k in keys:
		print(f'{extend_str(k.capitalize(), length[k])}', end=' '*4)
	print()
	for result in results:
		for k in keys:
			print(f'{extend_str(result[k], length[k])}', end=' '*4)
		print()


def test(function: Callable):
	path = f'test/{function.__name__}'

	# GETING ARGS FOR EVALUATION
	tests = request(path)

	# EVALUATING
	predictions = []
	for test in tests:
		start = time.perf_counter()
		result = function(*test['input'])
		stop = time.perf_counter()
		if result is not None:
			test['output'] = result
			test['time [sec]'] = round(stop - start, 10)
			predictions.append(test)

	# GETING RESULTS
	results = request(path, data=predictions)

	# PRINTING RESULTS
	print_results(results)
