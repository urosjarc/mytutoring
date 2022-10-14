import math
from typing import List


def vektor(x: int, y: int, z: int, i: int, j: int):
	"""
	Ustvari vektor v 5 dimenzijskem prostoru.
	:param x: X komponenta vektorja.
	:param y: Y komponenta vektorja.
	:param z: Z komponenta vektorja.
	:param i: 4 komponenta vektorja.
	:param j: 5 komponenta vektorja.
	:return: Vektor
	>>> vektor(1,-2,3,-4,5)
	[1, -2, 3, -4, 5]
	>>> vektor(5,2,-7,4,-2)
	[5, 2, -7, 4, -2]
	"""
	return [x, y, z, i, j]


def vektor_s_skalarjem(vektor: List[int], skalar: int):
	"""
	Pomnozi vektor z skalarjem.
	:param vektor: Vektor
	:param skalar: Stevilka ki predstavlja skalar.
	:return: Vektor pomnozen s skalarjem.
	>>> vektor_s_skalarjem([1,-2,9, 3, 8], 3)
	[3, -6, 27, 9, 24]
	>>> vektor_s_skalarjem([8,-3,-8, 3, 8, 0, 1], 3)
	[24, -9, -24, 9, 24, 0, 3]
	"""
	return [ele * skalar for ele in vektor]


def zrcaljenje_vektorja(vektor: List[int]):
	"""
	Obrni vektor da bo kazal v drugo smer.
	:param vektor: Vhodni vektor.
	:return: Obrnjen vektor.
	>>> zrcaljenje_vektorja([1,-2,9, 3, 8])
	[-1, 2, -9, -3, -8]
	>>> zrcaljenje_vektorja([8,-3,-8, 3, 8, 0, 1])
	[-8, 3, 8, -3, -8, 0, -1]
	"""
	return [-ele for ele in vektor]


def vsota_vektorja(vektor1: List[int], vektor2: List[int]):
	"""
	Izracunaj vsoto dveh vektorjev.
	:param vektor1: Prvi vektor.
	:param vektor2: Drugi vektor.
	:return: Vsota vektorjev.
	>>> vsota_vektorja([1,2,3], [3, -2, -1])
	[4, 0, 2]
	>>> vsota_vektorja([1,2,3,4,5], [1,2,3])
	[2, 4, 6, 4, 5]
	>>> vsota_vektorja([1,2], [1,2,3, 8, 2, -23])
	[2, 4, 3, 8, 2, -23]
	"""
	if len(vektor1) > len(vektor2):
		for i in range(len(vektor2)):
			vektor1[i] += vektor2[i]
		return vektor1
	else:
		for i in range(len(vektor1)):
			vektor2[i] += vektor1[i]
		return vektor2


def velikost_vektorja(vektor: List[int]):
	"""
	Izracunaj velikost vektorja.
	:param vektor: Vektor
	:return: Velikost vektorja.
	>>> velikost_vektorja([1,2,3])
	3.741657
	>>> velikost_vektorja([1,-2,3, 1, 9])
	9.797959
	"""
	vektor = [ele ** 2 for ele in vektor]
	return round(sum(vektor) ** 0.5, 6)


def oddaljenost_vektorja(v1: List[int], v2: List[int]):
	"""
	Izracunaj za koliko sta vektorja oddaljena drug od drugega.
	:param v1: Prvi vektor.
	:param v2: Drugi vektor.
	:return: Oddaljenost vektorja.
	>>> oddaljenost_vektorja([1, 2, 3], [3, 2, 1, 2, 3, 8])
	[4, 4, 4, 2, 3, 8]
	>>> oddaljenost_vektorja([3, 2, 1, 2, 3, 8], [-1, -2, 3])
	[2, 0, 4, 2, 3, 8]
	"""
	if len(v1) > len(v2):
		for i in range(len(v2)):
			v1[i] += v2[i]
		return v1
	else:
		for i in range(len(v1)):
			v2[i] += v1[i]
		return v2


def normalizacija_vektorja(v: List[int]):
	"""
	Ustvari normaliziran vektor.
	:param v: Vektor
	:return: Normaliziran vektor.
	>>> normalizacija_vektorja([1,2,3])
	[0.2673, 0.5345, 0.8018]
	>>> normalizacija_vektorja([-1,2,-3, 5, 9])
	[-0.0913, 0.1826, -0.2739, 0.4564, 0.8216]
	"""
	s = [ele ** 2 for ele in v]
	s = sum(s) ** 0.5
	return [round(ele / s, 4) for ele in v]


def mapiranje_vektorja(v: List[int]):
	"""
	Skaliraj vektor tako da bo max vrednost vektorja 1 in min element 0!
	:param v: Vektor
	:return: Skaliran vektor.
	>>> mapiranje_vektorja([1,2,3,4])
	[0.0, 0.3333, 0.6667, 1.0]
	>>> mapiranje_vektorja([-1,2,-3, 5, 9])
	[0.1667, 0.4167, 0.0, 0.6667, 1.0]
	"""
	m = min(v)
	M = max(v)
	k = 1 / (M - m)
	return [round(ele * k - k * m, 4) for ele in v]


def kot_vektorja(v1: List[int], v2: List[int]):
	"""
	Izracunaj kot med vektorjema.
	:param v1: Prvi vektor.
	:param v2: Drugi vektor.
	:return: Kot med vektorjema.
	>>> kot_vektorja([1,2,3], [1,2,3,4])
	75.03678
	>>> kot_vektorja([1,-2,3, 8, 1], [1,2,3,4])
	82.66699
	"""
	if len(v1) > len(v2):
		for i in range(len(v2)):
			v2[i] *= v1[i]
		up = sum(v2)
	else:
		for i in range(len(v1)):
			v1[i] *= v2[i]
		up = sum(v1)

	abs_v1 = [ele ** 2 for ele in v1]
	abs_v2 = [ele ** 2 for ele in v2]
	abs_v1 = sum(abs_v1) ** 0.5
	abs_v2 = sum(abs_v2) ** 0.5

	return round(math.degrees(math.acos(up / (abs_v1 * abs_v2))), 5)


def rotacija_vektorja_2D(v1: List[int], deg: float):
	"""
	Rotiraj vektor okoli drugega vektorja za specificni kot.
	:param v1: Prvi vektor.
	:param os: Os rotacije.
	:param deg: Kot rotacije v stopinjah.
	:return: Rotiran vektor okoli osi.
	>>> rotacija_vektorja_2D([1,2], 180)
	[-1.0, 2.0]
	>>> rotacija_vektorja_2D([1,2], 30)
	[-0.134, -1.2321]
	>>> rotacija_vektorja_2D([2,-1], -30)
	[1.2321, -0.134]
	>>> rotacija_vektorja_2D([2,-1], -180)
	[-2.0, -1.0]
	"""
	rad = math.radians(deg)
	return [
		round(v1[0]*math.cos(rad) - v1[1]*math.sin(rad), 4),
		round(v1[0]*math.sin(rad) - v1[1]*math.cos(rad), 4)
	]
