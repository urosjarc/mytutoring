def naravno_zaporedje(a: int, b: int):
	"""
	Ipisi zaporedje naravnih stevil od prve do druge stevilke.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	>>> naravno_zaporedje(-5, 5) # doctest: +NORMALIZE_WHITESPACE
	-5 -4 -3 -2 -1 0 1 2 3 4 5
	>>> naravno_zaporedje(3, 8) # doctest: +NORMALIZE_WHITESPACE
	 3 4 5 6 7 8
	"""
	for i in range(a, b + 1):
		print(i, end=' ')


def obratno_naravno_zaporedje(a: int, b: int):
	"""
	Ipisi obratno zaporedje naravnih stevil od prve do druge stevilke.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	>>> obratno_naravno_zaporedje(5, -5) # doctest: +NORMALIZE_WHITESPACE
	5 4 3 2 1 0 -1 -2 -3 -4 -5
	>>> obratno_naravno_zaporedje(8, 3) # doctest: +NORMALIZE_WHITESPACE
	8 7 6 5 4 3
	"""
	for i in range(a, b - 1, -1):
		print(i, end=' ')


def naravno_zaporedje_s_korakom(a: int, b: int):
	"""
	Ipisi zaporedje naravnih stevil od prve do druge stevilke s korakom 3.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	>>> naravno_zaporedje_s_korakom(-5, 7) # doctest: +NORMALIZE_WHITESPACE
	-5 -2 1 4 7
	>>> naravno_zaporedje_s_korakom(0, 10) # doctest: +NORMALIZE_WHITESPACE
	0 3 6 9
	"""
	for i in range(a, b + 1, 3):
		print(i, end=' ')


def aritmeticno_zaporedje(a0: int, d: int, n: int):
	"""
	Izpisi n clenov aritmeticnega zaporedja.
	:param a0: Zacetni clen.
	:param d: Diferenca zaporedja.
	:param n: Stevilo clenov za ispisati.
	>>> aritmeticno_zaporedje(3, 5, 8)  # doctest: +NORMALIZE_WHITESPACE
	3 8 13 18 23 28 33 38
	>>> aritmeticno_zaporedje(-8, -50, 5)
	-8 -58 -108 -158 -208
	"""
	for i in range(n):
		print(a0 + i * d, end=' ')


def geometrijsko_zaporedje(a0: int, k: int, n: int):
	"""
	Izpisi n clenov geometrijskega zaporedja.
	:param a1: Zacetni clen.
	:param k: Kolicnik zaporedja.
	:param n: Stevilo clenov za ispisati.
	>>> geometrijsko_zaporedje(3, 5, 8)  # doctest: +NORMALIZE_WHITESPACE
	3 15 75 375 1875 9375 46875 234375
	>>> geometrijsko_zaporedje(-8, -50, 5)  # doctest: +NORMALIZE_WHITESPACE
	-8 400 -20000 1000000 -50000000
	"""
	for i in range(n):
		print(a0 * k ** i, end=' ')


def alternirajoce_aritmeticno_zaporedje(a0: int, d: int, n: int):
	"""
	Izpisi n clenov alternirajocega zaporedja.
	:param a0: Zacetni clen.
	:param n: Stevilo clenov.
	:param d: Diferenca zaporedja.
	>>> alternirajoce_aritmeticno_zaporedje(3, 5, 8)  # doctest: +NORMALIZE_WHITESPACE
	3 -8 13 -18 23 -28 33 -38
	>>> alternirajoce_aritmeticno_zaporedje(-8, -50, 5)  # doctest: +NORMALIZE_WHITESPACE
	-8 58 -108 158 -208
	"""
	for i in range(n):
		print(((-1) ** i) * (a0 + i * d), end=' ')


def fibonacijevo_zaporedje(a: int, b:int, n: int):
	"""
	Izpisi n clenov fibonacijevega zaporedja.
	:param a: Zacetni clen.
	:param b: Naslednji clen
	:param n: Stevilo clenov.
	>>> fibonacijevo_zaporedje(0, 1, 10)  # doctest: +NORMALIZE_WHITESPACE
	0 1 1 2 3 5 8 13 21 34
	>>> fibonacijevo_zaporedje(5, 10, 8)  # doctest: +NORMALIZE_WHITESPACE
	5 10 15 25 40 65 105 170
	"""
	for i in range(n):
		print(a, end=' ')
		c = b + a
		a = b
		b = c
