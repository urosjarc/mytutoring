def vrednost_funkcije(x: float, k: float, a: float):
	"""
	Izracunaj vrednost linearne funkcije: f(x) = kx + a.
	:param x: Pozicija x.
	:param k: Smerni koelificijent.
	:param a: Zacetna vrednost.
	:return: Vrednost funckije v tocki x.
	"""
	return k * x + a


def tabela_funkcije(x0: float, x1: float, dx: float, a: float, b: float, c: float):
	"""
	Izpisi tabelo vrednosti polinoma: f(x) = ax^2 + bx + c
	Tabelo izpisi za vsak x med x0 in x1 s korakom dx.
	:param x0: Zacetni x.
	:param x1: Koncni x.
	:param dx: korak zaporedja.
	:param a: Parameter polinoma.
	:param b: Parameter polinoma.
	:param c: Parameter polinoma.
	>>> tabela_funkcije(1.0, 2.0, 0.2, 1., 1., 1.)   # doctest: +NORMALIZE_WHITESPACE
	1.0 3.0
	1.2 3.64
	1.4 4.36
	1.6 5.16
	1.8 6.04
	2.0 7.0
	>>> tabela_funkcije(1.0, 3.0, 0.1, 2., 0.1, 5.3)   # doctest: +NORMALIZE_WHITESPACE
	1.0	7.4
	1.1	7.83
	1.2	8.3
	1.3	8.81
	1.4	9.36
	1.5	9.95
	1.6	10.58
	1.7	11.25
	1.8	11.96
	1.9	12.71
	2.0	13.5
	2.1	14.33
	2.2	15.2
	2.3	16.11
	2.4	17.06
	2.5	18.05
	2.6	19.08
	2.7	20.15
	2.8	21.26
	2.9	22.41
	3.0	23.6
	"""
	while True:
		print(round(x0, 2), round(a * (x0 ** 2) + b * x0 + c, 2), sep='\t')
		if x0 + dx / 2 >= x1:
			break
		x0 += dx


def globalni_maximum(x0: float, x1: float, dx: float, a: float, b: float, c: float):
	"""
	Poisci globalni maximum polinoma med x0 in x1.
	:param x0: Zacetni x.
	:param x1: Koncni x.
	:param dx: korak zaporedja.
	:param a: Parameter polinoma.
	:param b: Parameter polinoma.
	:param c: Parameter polinoma.
	>>> globalni_maximum(0, 1, 0.0001, -1, 0, 0)   # doctest: +NORMALIZE_WHITESPACE
	0.0
	>>> globalni_maximum(0, 1, 0.0001, 1, 0, 0)   # doctest: +NORMALIZE_WHITESPACE
	1.0
	>>> globalni_maximum(0, 1, 0.0001, -10, 10, -1.8)   # doctest: +NORMALIZE_WHITESPACE
	0.7
	>>> globalni_maximum(0, 1, 0.001, -10, 9, -1)   # doctest: +NORMALIZE_WHITESPACE
	1.025
	"""
	maxy = a * (x0 ** 2.0) + b * x0 + c
	while True:
		y = a * (x0 ** 2.0) + b * x0 + c
		if y > maxy:
			maxy = y
		x0 += dx
		if x0 > x1:
			break

	return round(maxy, 7)


def nicla_funkcije(x0: float, x1: float, dx: float, a: float, b: float, c: float):
	"""
	Poisci niclo polinoma med x0 in x1.
	:param x0: Zacetni x.
	:param x1: Koncni x.
	:param dx: korak zaporedja.
	:param a: Parameter polinoma.
	:param b: Parameter polinoma.
	:param c: Parameter polinoma.
	>>> nicla_funkcije(0, 1, 0.0001, 1, 0, 0)   # doctest: +NORMALIZE_WHITESPACE
	0
	>>> nicla_funkcije(0, 1, 0.0001, 1, -2, 1)   # doctest: +NORMALIZE_WHITESPACE
	1.0
	>>> nicla_funkcije(0, 1, 0.001, 1, -1.3, .1)   # doctest: +NORMALIZE_WHITESPACE
	0.082
	"""
	miny = abs(a * (x0 ** 2) + b * x0 + c)
	x = x0
	while True:
		y = a * (x0 ** 2) + b * x0 + c
		if abs(y) < miny:
			miny = abs(y)
			x = x0
		x0 += dx
		if x0 + dx / 2 > x1:
			break

	return round(x, 3)
