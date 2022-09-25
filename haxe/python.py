"""
This is module docs...
"""
import json
from typing import List


def encode(data):
	if isinstance(data, int | float):
		return str(data)
	elif isinstance(data, bool):
		return str(data).lower()
	elif isinstance(data, str):
		return f'"{data}"'
	elif isinstance(data, list):
		if len(data) != 0:
			s = '['
			for d in data:
				s += f'{encode(d)}, '
			return s[:-2] + ']'
		else:
			return '[]'
	else:
		if hasattr(data, '__dict__'):
			data = data.__dict__
		if len(data) != 0:
			s = '{'
			for k, v in data.items():
				s += f'"{k}": {encode(v)}, '
			return s[:-2] + '}'
		else:
			return '{}'


def decode(string):
	return json.loads(string)

def exercise_00(root: int) -> int:
	f"""
	Vrni stevilo node/ov.
	:param a: /
	:return: a+b

	{root},6
	{root},6
	{root},6
	{root},6
	"""
	return int()


def exercise_01(a: int, b: int) -> int:
	"""
	Vrni vsoto stevil.
	:param a: /
	:param b: /
	:return: a+b

	5,6,11
	0,1,1
	-6,-2,-8
	-2,3,1
	"""
	return a + b
