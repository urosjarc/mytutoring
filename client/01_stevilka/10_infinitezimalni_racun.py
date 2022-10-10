def odvod_funkcije(x0: float, x1: float, dx: float, a: float, b: float, c: float):
	"""
	Izracunaj tabelo vrednosti odvoda polinoma: f(x) = ax^2 + bx + c
	:param x0: Zacetni x.
	:param x1: Koncni x.
	:param dx: Korak iskanja.
	:param a: Polinomski koelificijent.
	:param b: Polinomski koelificijent.
	:param c: Polinomski koelificijent.
	:param d: Polinomski koelificijent.
	>>> odvod_funkcije(0, 1, 0.1, 1, 1, 1)
	0 1.1
	0.1 1.3
	0.2 1.5
	0.3 1.7
	0.4 1.9
	0.5 2.1
	0.6 2.3
	0.7 2.5
	0.8 2.7
	0.9 2.9
	1.0 3.1
	>>> odvod_funkcije(0, 1, 0.05, 2, -1, 1)
	0 -0.9
	0.05 -0.7
	0.1 -0.5
	0.15 -0.3
	0.2 -0.1
	0.25 0.1
	0.3 0.3
	0.35 0.5
	0.4 0.7
	0.45 0.9
	0.5 1.1
	0.55 1.3
	0.6 1.5
	0.65 1.7
	0.7 1.9
	0.75 2.1
	0.8 2.3
	0.85 2.5
	0.9 2.7
	0.95 2.9
	1.0 3.1
	"""
	f = lambda x: a * (x ** 2) + b * x + c
	while True:
		dy = (f(x0 + dx) - f(x0)) / dx
		print(round(x0, 3), round(dy, 3))
		if x0 + dx / 2 >= x1:
			break
		x0 += dx


def lokalni_maximum(x0: float, x1: float, dx: float, a: float, b: float, c: float, d: float):
	"""
	Izpisi vse lokalne maximume in minimume med x0 in x1 s korakom dx.
	:param x0: Zacetni x.
	:param x1: Koncni x.
	:param dx: Korak iskanja.
	:param a: Polinomski koelificijent.
	:param b: Polinomski koelificijent.
	:param c: Polinomski koelificijent.
	:param d: Polinomski koelificijent.
	>>> lokalni_maximum(-5, 5, 0.0001,-0.3, 1, 1.4, -2)
	-0.559
	2.781
	>>> lokalni_maximum(-5, 5, 0.0001,-0.2, -1, 1.2, 3)
	-3.853
	0.519
	"""
	f = lambda x: a * (x ** 3) + b * (x ** 2) + c * x + d
	while True:
		dy = (f(x0 + dx) - f(x0)) / dx
		if abs(dy) < dx:
			print(round(x0, 3))
		if x0 + dx / 2 >= x1:
			break
		x0 += dx


def integral(x0: float, x1: float, dx: float, a: float, b: float, c: float, d: float):
	"""
	Izracunaj integral polinoma.
	:param x0: Zacetni x.
	:param x1: Koncni x.
	:param dx: Korak iskanja.
	:param a: Polinomski koelificijent.
	:param b: Polinomski koelificijent.
	:param c: Polinomski koelificijent.
	:param d: Polinomski koelificijent.
	>>> integral(-5, 5, 0.0001,-0.3, 1, 1.4, -2)
	63.336
	>>> integral(-5, 5, 0.0001,-0.2, -1, 1.2, 3)
	-53.331
	"""
	f = lambda x: a * (x ** 3) + b * (x ** 2) + c * x + d
	p = 0
	while True:
		y = f(x0)
		p += y * dx
		x0 += dx
		if x0 > x1:
			break
	return round(p, 3)


def domet(dt: float, x0: float, y0: float, z0: float, vx: float, vy: float, vz: float):
	"""
	Izpiši domet in najvišjo višino izstrelka in pozicijo (x, y, z) trka z tlemi.
	Upostevaj da je gravitacija -9.81 m/s^2
	:param dt: Casovni korak simulacije.
	:param x0: Zacetna x pozicija.
	:param y0: Zacetna y pozicija.
	:param z0: Zacetna visina.
	:param vx: Zacetna hitrost izstrelka po x osi.
	:param vy: Zacetna hitrost izstrelka po y osi.
	:param vz: Zacetna hitrost izstrelka po z osi.
	>>> domet(0.001, 0, 0, 1, 1, 1, 1)
	Domet: 0.799 m
	Visina: 1.05 m
	Pozicija: (0.565, 0.565, -0.004)
	>>> domet(0.001, -1, -3, 1, 2, -1, 10)
	Domet: 6.086 m
	Visina: 6.092 m
	Pozicija: (3.268, -5.134, -0.008)
	"""
	x, y, z = x0, y0, z0
	zMax = z
	while z > 0:
		vz += -9.81 * dt

		x += vx * dt
		y += vy * dt
		z += vz * dt

		if z > zMax:
			zMax = z

	print(f'Domet: {round((x**2 + y**2)**0.5, 3)} m')
	print(f'Visina: {round(zMax, 3)} m')
	print(f'Pozicija: ({round(x, 3)}, {round(y, 3)}, {round(z, 3)})')
