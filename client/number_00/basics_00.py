"""
This is module docs
"""

import random
import math


def apokalipsa(a: int) -> int:
	"""
	Izpisi stevilo ki ga dobis ce vneseno stevilo...
	:param a: Parameter notri
	:return: Element
	"""
	return a + 5


def test(a: int) -> int:
	"""
	Izpisi stevilo ki ga dobis ce vneseno stevilo...

	:param a: Parameter notri
	:return: Element
	"""
	return a + 5


if __name__ == '__main__':
	assert apokalipsa(10) == 14
	assert test(10) == 15
