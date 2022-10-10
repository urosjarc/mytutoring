def delitelji(a: int):
	"""
	Uporabnik vnese število.
	Izpiši vse delitelje števila.
	:param a: Stevilo.
	>>> delitelji(24*4) # doctest: +NORMALIZE_WHITESPACE
	1 2 3 4 6 8 12 16 24 32 48 96
	>>> delitelji(7)  # doctest: +NORMALIZE_WHITESPACE
	1 7
	"""
	for i in range(1, a + 1):
		if a % i == 0:
			print(i, end=' ')


def prastevilo(a: int):
	"""
	Preveri ce je stevilo prastevilo.
	:param a: Stevilo.
	:return: True/False
	>>> prastevilo(1)
	True
	>>> prastevilo(2)
	False
	>>> prastevilo(3)
	True
	>>> prastevilo(4)
	False
	>>> prastevilo(5)
	True
	>>> prastevilo(6)
	False
	>>> prastevilo(71)
	True
	>>> prastevilo(120)
	False
	"""
	if a == 2:
		return False
	for i in range(2, a):
		if a % i == 0:
			return False

	return True


def ugani_stevilo(a: int):
	r"""
	Uporabnik naj ugiba število dokler ga ne ugane.
	Na koncu vrni število poskusov ki jih je uporabnik naredil.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n10')
	>>> ugani_stevilo(10)
	6
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n2\n3\n66')
	>>> ugani_stevilo(66)
	8
	"""
	c = 0
	while True:
		b = int(input())
		c += 1
		if b == a:
			break
	return c


def povprecje():
	r"""
	Uporabnik vnaša števila dokler ne vnese števila nič.
	Izracunaj povprecje stevil ki jih je uporabnik vnesel.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n10\n0')
	>>> povprecje()
	3.0
	>>> sys.stdin = io.StringIO('1\n3\n6\n200\n0\n2\n3\n66\n0')
	>>> povprecje()
	52.5
	"""
	v = []
	while True:
		a = int(input())
		if a == 0:
			break
		v.append(a)
	return round(sum(v) / len(v), 6)


def vecje_od_prejsnje():
	r"""
	Uporabnik vnasa stevilke dokler ne vnese stevila nic.
	Izpisi stevilo ce je vecje od prejsnjega stevila.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n5\n1\n4\n0\n10\n0')
	>>> vecje_od_prejsnje()  # doctest: +NORMALIZE_WHITESPACE
	3 6 5 4
	>>> sys.stdin = io.StringIO('3\n1\n6\n2\n10\n2\n3\n66\n0')
	>>> vecje_od_prejsnje()  # doctest: +NORMALIZE_WHITESPACE
	6 10 3 66
	"""
	p = int(input())
	while True:
		a = int(input())
		if a == 0:
			break
		elif a > p:
			print(a, end=' ')
		p = a


def max_stevilo():
	r"""
	Uporabnik vnaša števila dokler ne vnese števila nič.
	Izpiši maksimalno stevilo in na katerem mestu se je pojavila.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n10\n0')
	>>> max_stevilo()
	Maks stevilo: 6
	Mesto stevilke: 3
	>>> sys.stdin = io.StringIO('1\n3\n6\n200\n0\n2\n3\n66\n0')
	>>> max_stevilo()
	Maks stevilo: 200
	Mesto stevilke: 4
	>>> sys.stdin = io.StringIO('-10\n-30\n-6\n-10\n-20\n-30\n-60\n0')
	>>> max_stevilo()
	Maks stevilo: -6
	Mesto stevilke: 3
	"""
	c = 1
	m = int(input())
	i = 0
	while True:
		b = int(input())
		if b == 0:
			break
		if b > m:
			m = b
			i = c + 1
		c += 1
	print(f'Maks stevilo: {m}')
	print(f'Mesto stevilke: {i}')
