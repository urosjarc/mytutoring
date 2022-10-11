import math


def vsota(a: int, b: int):
	"""
	Izracunaj vsoto stevil od prve do druge stevilke.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Vsota stevil.
	>>> vsota(0, 100)
	5050
	>>> vsota(0, 10)
	55
	>>> vsota(-5, 10)
	40
	"""
	return sum([i for i in range(a, b + 1)])


def vsota_uporabniskih_stevilk(n: int):
	r"""
	Uporabnik vnasa n nakljucnih stevil.
	Izracunaj vsoto vnesenih stevil.
	:param n: Stevilo stevil ki jih bo uporabnik vnesel.
	:return: Vsota stevil.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2')
	>>> vsota_uporabniskih_stevilk(4)
	12
	>>> sys.stdin = io.StringIO("3\n6\n2")
	>>> vsota_uporabniskih_stevilk(3)
	11
	"""
	return sum([int(input()) for i in range(n)])


def vsota_do_nic():
	r"""
	Uporabnik vnasa nakljucna stevila dokler ne vnese stevilo 0.
	Izracunaj vsoto vnesenih stevil.
	:return: Vsota stevil.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n3')
	>>> vsota_do_nic()
	12
	>>> sys.stdin = io.StringIO("3\n6\n2\n0\n2")
	>>> vsota_do_nic()
	11
	"""
	v = 0
	while True:
		a = int(input())
		if a == 0:
			break
		v += a
	return v


def aritmeticna_vsota(a0: int, d: int, n: int):
	"""
	Izracunaj aritmeticno vsoto zaporedja.
	:param a0: Zacetni clen.
	:param d: Diferenca zaporedja.
	:param n: Stopnja zaporedja.
	:return: Vsota zaporedja.
	>>> aritmeticna_vsota(1, 1, 10)
	55
	>>> aritmeticna_vsota(1, 1, 100)
	5050
	>>> aritmeticna_vsota(3, 3, 100)
	15150
	"""
	return round(sum([a0 + d * i for i in range(n)]))


def taylor_vsota(n: int):
	"""
	Z taylorjevo vsoto izracunaj eulerjevo konstanto.
	e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ...
	:param n: Stopnja vsote.
	:return: Eulerjeva konstanta.
	>>> taylor_vsota(5)
	2.70833
	>>> taylor_vsota(10)
	2.71828
	>>> taylor_vsota(20)
	2.71828
	"""
	return round(sum([1 / math.factorial(i) for i in range(n)]), 5)


def gregory_leibniz_vsota(n: int):
	"""
	Izracunaj pi z Gregory Leibniz vsoto do n-tega clena.
	:param n: Stopnja vsote.
	:return: Vrednost pi-ja
	>>> gregory_leibniz_vsota(20)
	3.091624
	>>> gregory_leibniz_vsota(200)
	3.136593
	>>> gregory_leibniz_vsota(2000)
	3.141093
	"""
	v = 0
	for i in range(n):
		v += ((-1) ** i) / (2 * i + 1)
	return round(v * 4, 6)


def sin_vsota(x: float, n: int):
	"""
	Izracunaj sinus z uporabo sinusne vsote.
	sin(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + ...
	:param n: Stopnja vsote.
	:return: Vrednost sinusa v x-u.
	>>> sin_vsota(0, 10)
	0.0
	>>> sin_vsota(math.pi/6, 10)
	0.5
	>>> sin_vsota(math.pi/4, 10)
	0.707107
	>>> sin_vsota(math.pi/3, 10)
	0.866025
	>>> sin_vsota(math.pi/2, 10)
	1.0
	"""
	v = 0
	for i in range(n):
		v += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
	return round(v, 6)
