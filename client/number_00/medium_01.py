def test3(a: int) -> int:
	"""
	Izpisi stevilo ki ga dobis ce vneseno stevilo...
	:param a: Parameter notri
	:return: Element
	"""
	return a+5

def test5(a: int) -> int:
	"""
	Izpisi stevilo ki ga dobis ce vneseno število...
	:param a: Parameter notri
	:return: Element
	"""
	return a+5

if __name__ == '__main__':
	assert test3(10) == 15
	assert test5(10) == 15
