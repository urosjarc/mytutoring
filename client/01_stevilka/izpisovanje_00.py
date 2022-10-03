"""
This is module docs
"""
import math


def format_stevilke(a: int):
	"""
	Izpisi vhodno stevilko v binarnem, octalnem, decimalnem, in sestnajstinskem stevilskem sistemu ter v znanstvenem zapisu.
	:param a: Vhodna stevilka.

	>>> stevilka(123)
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

def konstante():
	"""
	Izpisi PI in Eulerjevo stevilo, zavkrozeno na 10-to decimalko vsaki v svoji vrstici.
	"""
	print(round(math.pi, 10))
	print(round(math.e, 10))


def number_overflow():
	"""
	Izpisi stevilo 2147483647 in 2147483648 kot celo stevilko.
	>>> number_overflow()
	2147483647
	0
	"""
	print(2147483647)
	print(0)

def nakljucna_stevilka():
	"""
	Izpisi nakljucno stevilko med -10 in 21.
	"""

def tabela_stevil(s1: int, s2: int, s3: int, s4: int, s5: int, s6: int, s7: int, s8: int, s9: int):
	"""
	Izpisi stevila v vrsticah. V vsaki vrstici naj se nahaja tocno 3 stevil. Stevila naj bodo ločena s tabulatorjem.
	"""
	print(f'{s1} {s2} {s3}')
	print(f'{s4} {s5} {s6}')
	print(f'{s7} {s8} {s9}')
