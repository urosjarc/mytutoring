import math


def vsota(a: int, b: int):
	"""
	Izracunaj vsoto.
	:param a: Leva stevilka.
	:param b: Desna stevilka.
	:return: Vsota stevilk.
	>>> vsota(3,5)
	8
	>>> vsota(12, 63)
	75
	"""
	return a + b


def minus(a: int, b: int):
	"""
	Izracunaj razliko.
	:param a: Leva stevilka.
	:param b: Desna stevilka.
	:return: Razlika stevil.
	>>> minus(3, 23)
	-20
	>>> vsota(8,3)
	5
	"""
	return a - b


def zmnozek(a: int, b: int):
	"""
	Izracunaj zmnozek stevil.
	:param a: Leva stevilka.
	:param b: Desna stevilka.
	:return: Zmanozek stevil.
	>>> zmnozek(3, 5)
	15
	>>> zmnozek(5,7)
	35
	"""
	return a * b


def kolicnik(a: int, b: int):
	"""
	Izracunaj kolicnik stevil.
	:param a: Stevec
	:param b: Imenovalec
	:return: Razmerje stevca in imenovalca.
	>>> kolicnik(15, 3)
	5.0
	>>> kolicnik(30, 4)
	7.5
	"""
	return a / b


def celo_stevilsko_deljenje(a: int, b: int):
	"""
	Izracunaj celo številski kolicnik.
	:param a: Levo stevilo.
	:param b: Desno stevilo.
	:return: Celo stevilski kolicnik.
	>>> celo_stevilsko_deljenje(15, 3)
	5
	>>> celo_stevilsko_deljenje(30, 4)
	7
	"""
	return a // b


def modulo(a: int, b: int):
	"""
	Izracunaj modulo (ostanek pri deljenju)
	:param a: Levo stevilo.
	:param b: Desno stevilo.
	:return: Modulo stevila.
	>>> modulo(15, 3)
	0
	>>> modulo(30, 4)
	2
	"""
	return a % b


def potenca(a: int, b: int):
	"""
	Izracunaj potenco stevila.
	:param a: Osnova.
	:param b: Exponent
	:return: Rezultat potenciranja.
	>>> potenca(15, 3)
	3375
	>>> potenca(30, 4)
	810000
	"""
	return a ** b


def koren(a: int, b: int):
	"""
	Izracunaj koren stevila.
	:param a: Osnova.
	:param b: Koren.
	:return: Rezultat korenjenja.
	>>> koren(15, 3)
	2.47
	>>> koren(30, 4)
	2.34
	"""
	return round(a ** (1 / b),2)


def absolutna_vrednost(a: int):
	"""
	Izracunaj absolutno vrednost stevila.
	:param a: Stevilo.
	:return: Absolutna vrednost.
	>>> absolutna_vrednost(-5)
	5
	>>> absolutna_vrednost(5)
	5
	"""
	return abs(a)


def logaritem(a: float, b: float):
	"""
	Izracunaj logaritem osnove in stopnje.
	:param a: Osnova.
	:param b: Stopnja.
	:return: Rezultat logaritma osnove in stopnje.
	>>> logaritem(15, 3)
	2.46
	>>> logaritem(30, 4)
	2.45
	"""
	return round(math.log(a, b), 2)


def fakulteta(a: int):
	"""
	Izracunaj fakulteto stevila.
	:param a: Stevilo.
	:return: Fakulteta stevila.
	>>> fakulteta(5)
	120
	>>> fakulteta(7)
	5040
	"""
	return math.factorial(a)
