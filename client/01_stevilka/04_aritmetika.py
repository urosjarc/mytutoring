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
	>>> zmnozek()
	"""
	return a * b


def kolicnik(a: int, b: int):
	"""
	Izracunaj kolicnik stevil.
	:param a:
	:param b:
	:return:
	"""
	return a / b


def celo_stevilsko_deljenje(a: int, b: int):
	"""
	Izracunaj celo številski kolicnik.
	:param a: Levo stevilo.
	:param b: Desno stevilo.
	:return: Celo stevilski kolicnik.
	"""
	return a // b


def modulo(a: int, b: int):
	"""
	Izracunaj modulo (ostanek pri deljenju)
	:param a: Levo stevilo.
	:param b: Desno stevilo.
	:return: Modulo stevila.
	"""
	return a % b


def potenca(a: int, b: int):
	"""
	Izracunaj potenco stevila.
	:param a: Osnova.
	:param b: Exponent
	:return: Rezultat potenciranja.
	"""
	return a ** b


def koren(a: int, b: int):
	"""
	Izracunaj koren stevila.
	:param a: Osnova.
	:param b: Koren.
	:return: Rezultat korenjenja.
	"""
	return a ** 1 / b


def absolutna_vrednost(a: int):
	"""
	Izracunaj absolutno vrednost stevila.
	:param a: Stevilo.
	:return: Absolutna vrednost.
	"""
	return abs(a)


def logaritem(a: float, b: float):
	"""
	Izracunaj logaritem osnove in stopnje.
	:param a: Osnova.
	:param b: Stopnja.
	:return: Rezultat logaritma osnove in stopnje.
	"""
	return round(math.log(a, b))


def fakulteta(a: int):
	"""
	Izracunaj fakulteto stevila.
	:param a: Stevilo.
	:return: Fakulteta stevila.
	"""
	return math.factorial(a)
