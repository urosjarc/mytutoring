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


def ugani_število(a: int):
	r"""
	Uporabnik naj ugiba število dokler ga ne ugane.
	Na koncu izpiši število poskusov ki jih je uporabnik naredil.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n10')
	>>> ugani_število(10)
	6
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n2\n3\n66')
	>>> ugani_število(66)
	8
	"""
	c = 0
	while True:
		b = int(input())
		c += 1
		if b == a:
			break
	return c


def stevila_do_nicle():
	r"""
	Uporabnik vnaša števila dokler ne vnese števila nič.
	Izpiši...
	* Število vnesenih števil
	* Max število
	* Katero število v vrsti je bilo maksimalno število.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('1\n3\n6\n2\n0\n10\n0')
	>>> stevila_do_nicle()
	Stevilo vnosov: 4
	Maks stevilo: 6
	Index maks stevilke: 3
	>>> sys.stdin = io.StringIO('1\n3\n6\n200\n0\n2\n3\n66\n0')
	>>> stevila_do_nicle()
	Stevilo vnosov: 4
	Maks stevilo: 200
	Index maks stevilke: 4
	>>> sys.stdin = io.StringIO('-10\n-30\n-6\n-10\n-20\n-30\n-60\n0')
	>>> stevila_do_nicle()
	Stevilo vnosov: 7
	Maks stevilo: -6
	Index maks stevilke: 3
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
			i = c+1
		c += 1
	print(f'Stevilo vnosov: {c}')
	print(f'Maks stevilo: {m}')
	print(f'Index maks stevilke: {i}')
