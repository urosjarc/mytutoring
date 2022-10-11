def naravno_zaporedje_naprej(zacetek: int, konec: int, korak: int):
	"""
	Ipisi zaporedje naravnih stevil od prve do druge stevilke z poljubnim korakom.
	:param zacetek: Prva stevilka.
	:param konec: Druga stevilka.
	:param korak: Korak zaporedja.
	>>> naravno_zaporedje_naprej(-5, 5, 1) # doctest: +NORMALIZE_WHITESPACE
	-5 -4 -3 -2 -1 0 1 2 3 4 5
	>>> naravno_zaporedje_naprej(3, 8, 2) # doctest: +NORMALIZE_WHITESPACE
	 3 5 7
	"""
	for i in range(zacetek, konec + 1, korak):
		print(i, end=' ')


def naravno_zaporedje_nazaj(zacetek: int, konec: int, korak: int):
	"""
	Ipisi obratno zaporedje naravnih stevil od prve do druge stevilke z poljubnim korakom.
	:param zacetek: Prva stevilka.
	:param konec: Druga stevilka.
	:param korak: Korak zaporedja.
	>>> naravno_zaporedje_nazaj(5, -5, 1) # doctest: +NORMALIZE_WHITESPACE
	5 4 3 2 1 0 -1 -2 -3 -4 -5
	>>> naravno_zaporedje_nazaj(8, 2, 2) # doctest: +NORMALIZE_WHITESPACE
	8 6 4 2
	"""
	for i in range(zacetek, konec - 1, -korak):
		print(i, end=' ')


def exponentno_zaporedje(osnova: int, n: int):
	"""
	Izpisi n clenov exponentnega zaporedja z poljubno osnovo.
	:param osnova: Poljubna cela stevilka.
	:param n: Stevilo clenov.
	>>> exponentno_zaporedje(2, 6) # doctest: +NORMALIZE_WHITESPACE
	1 2 4 8 16 32
	>>> exponentno_zaporedje(3, 6) # doctest: +NORMALIZE_WHITESPACE
	1 3 9 27 81 243
	"""
	for i in range(n):
		print(osnova ** i, end=" ")


def naravno_zaporedje(zacetek: int, konec: int, korak: int):
	"""
	Ipisi zaporedje naravnih stevil od zacetne do koncne stevilke s pozitivnim korakom.
	:param zacetek: Prva stevilka.
	:param konec: Druga stevilka.
	:param korak: Korak zaporedja [zmeraj pozitivna stevilka].
	>>> naravno_zaporedje(-5, 7, 1) # doctest: +NORMALIZE_WHITESPACE
	-5 -4 -3 -2 -1 0 1 2 3 4 5 6 7
	>>> naravno_zaporedje(10, 0, 1) # doctest: +NORMALIZE_WHITESPACE
	10 9 8 7 6 5 4 3 2 1 0
	>>> naravno_zaporedje(-5, 7, 3) # doctest: +NORMALIZE_WHITESPACE
	-5 -2 1 4 7
	>>> naravno_zaporedje(10, 0, 4) # doctest: +NORMALIZE_WHITESPACE
	10 6 2
	"""
	if zacetek > konec:
		konec -= 1
		korak *= -1
	else:
		konec += 1

	for i in range(zacetek, konec, korak):
		print(i, end=' ')


def aritmeticno_zaporedje(a0: int, d: int, n: int):
	"""
	Izpisi n clenov aritmeticnega zaporedja.
	:param a0: Zacetni clen.
	:param d: Diferenca zaporedja.
	:param n: Stevilo clenov za ispisati.
	>>> aritmeticno_zaporedje(3, 5, 8)  # doctest: +NORMALIZE_WHITESPACE
	3 8 13 18 23 28 33 38
	>>> aritmeticno_zaporedje(-8, -50, 5)  # doctest: +NORMALIZE_WHITESPACE
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


def fibonacijevo_zaporedje(a: int, b: int, n: int):
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
