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
				s+=f'{encode(d)}, '
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

def decode(obj):
	pass

class Test:
	def __init__(self):
		self.a = 'asf'

class Node:
	def __init__(self, value: int, name: str, children=None):
		self.value: int = value
		self.name: str = name
		self.child = Test()
		self.children: List[Node] = children
		if self.children is None:
			self.children = []
		self.test = {'test': 0, 'adf': Test()}

	def __str__(self):
		return encode(self)

	@staticmethod
	def parse(data: str|dict):
		if isinstance(data, str):
			data = json.dumps(data)
		return Node(value=data['value'], name=data['name'], children=[
			Node.parse(child_data) for child_data in data['children']
		])


root = Node(0, "nic", [
	Node(1, "ena"),
	Node(2, "dva", [
		Node(3, "tri"),
		Node(4, "stiri", [
			Node(5, "pet")
		]),
	])
])
print(str(root))
print(json.dumps(json.loads(str(root))))


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
