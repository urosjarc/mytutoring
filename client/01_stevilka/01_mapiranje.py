def str_int(a: str) -> float:
	"""
	Pretvori besedo v stevilko.
	:param a: Beseda
	:return: Decimalka
	>>> str_int('123.45')
	123.45
	>>> str_int('54.321')
	54.321
	"""
	return float(a)


def int_float(a: int):
	"""
	Pretvori celo stevilko v decimalko.
	:param a: Cela stevilka.
	:return: Decimalka.
	>>> int_float(123)
	123.0
	>>> int_float(1234)
	1234.0
	"""
	return float(a)


def float_int(a: float):
	"""
	Pretvori decimalko v celo stevilo.
	:param a: Decimalka.
	:return: Celo stevilo.
	>>> float_int(123.45)
	123
	>>> float_int(45.321)
	45
	"""
	return int(a)


def dec_bin(a: int) -> int:
	"""
	Pretvori celo stevilo v binarno stevilko.
	:param a: Cela stevilka.
	:return: Binarna stevilka
	>>> dec_bin(123)
	1111011
	>>> dec_bin(321)
	101000001
	"""
	return int(bin(a)[2:])


def dec_hex(a: int) -> str:
	"""
	Pretvori celo stevilo v binarno stevilko.
	:param a: Cela stevilka.
	:return: Hex stevilka.
	>>> dec_hex(123)
	'7b'
	>>> dec_hex(321)
	'141'
	"""
	return hex(a)[2:]


def bin_dec(a: int):
	"""
	Pretvori binarno stevilo v celo stevilo.
	:param a: Binarno stevilo.
	:return: Celo stevilo.
	>>> bin_dec(1111011)
	123
	>>> bin_dec(101000001)
	321
	"""
	return sum([int(e) * 2 ** i for i, e in enumerate(str(a)[::-1])])


def hex_dec(a: str):
	"""
	Pretvori hex stevilo v celo stevilo.
	:param a: Hex stevilo.
	:return: Celo stevilo.
	>>> hex_dec('7b')
	123
	>>> hex_dec('141')
	321
	"""
	return int(a, base=16)


def bin_hex(a: int):
	"""
	Pretvori binarno v decimalno stevilo.
	:param a: Binarno stevilo.
	:return: Decimalno stevilo.
	>>> bin_hex(1111011)
	'7b'
	>>> bin_hex(101000001)
	'141'
	"""
	return dec_hex(bin_dec(a))


def hex_bin(a: int):
	"""
	Pretvori hex v binarno stevilo.
	:param a: Hex stevilo.
	:return: Binarno stevilo.
	>>> hex_bin('7b')
	1111011
	>>> hex_bin('141')
	101000001
	"""
	return dec_bin(hex_dec(a))
