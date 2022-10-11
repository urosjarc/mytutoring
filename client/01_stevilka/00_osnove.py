"""
This is module docs
"""
import math
import random


def number_overflow():
	"""
	Izpisi stevilo 2147483647 in 2147483648 kot celo stevilko.
	>>> number_overflow()
	2147483647
	0
	"""
	print(2147483647)
	print(0)


def deljenje_z_niclo(a: int):
	"""
	Vrni stevilko ki jo dobiš če vhodno številko deliš z 0.
	:param a: Vhodna stevilka.
	:return: Rezultat.
	>>> deljenje_z_niclo(123)
	Traceback (most recent call last):
	...
	ZeroDivisionError: division by zero
	"""
	return a / 0


def format_stevilke(a: int):
	"""
	Izpisi vhodno stevilko v binarnem, octalnem, decimalnem, in sestnajstinskem stevilskem sistemu ter v znanstvenem zapisu.
	:param a: Vhodna stevilka.

	>>> format_stevilke(123)
	Bin: 0b1111011
	Oct: 0o173
	Dec: 123
	Hex: 0x7b
	Sci: 1.230000e+02
	"""
	print(f'Bin: {bin(a)}')
	print(f'Oct: {oct(a)}')
	print(f'Dec: {a}')
	print(f'Hex: {hex(a)}')
	print(f'Sci: {a:e}')


def zapis_stevilke():
	"""
	Iz funkcije vrni rezultat racuna: 0b1111011 + 0o173 - 123 - 0x7b + 1.230000e+02
	:return: Rezultat racuna.
	>>> print(zapis_stevilke())
	123.0
	"""
	return 0b1111011 + 0o173 - 123 - 0x7b + 1.230000e+02


def nakljucna_stevilka():
	"""
	Poisci nakljucno stevilko za katero velja: -10 <= x <= 21.
	>>> for i in range(100):
	...     assert -10 <= nakljucna_stevilka() <= 21
	"""
	return random.randint(-10, 21)


def zaokrozevanje():
	"""
	Izpisi PI in Eulerjevo stevilo, zavkrozeno na 10-to decimalko vsaki v svoji vrstici.
	>>> zaokrozevanje()
	3.1415926536
	2.7182818285
	"""
	print(round(math.pi, 10))
	print(round(math.e, 10))
