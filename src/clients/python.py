from typing import Callable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def url(path):
	return f'http://localhost:5000/{path}'

def get_test():
	pass

def test(function: Callable):
	post_fields = {'foo': 'bar'}
	request = Request(url(f'test/{function.__name__}'), data=urlencode(post_fields).encode())
	json = urlopen(request).read().decode()
	print(json)
