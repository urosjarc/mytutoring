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
	vektor = [ele**2 for ele in vektor]
	return round(sum(vektor)**0.5, 6)



def oddaljenost_vektorja():
	"""
	Ustvari dva spiska ki predstavljata vektorja v 8 dimenzijskem prostoru.
	Izračunaj za koliko sta oddaljena drug od drugega.
	"""
	pass


def normalizacija_vektorja():
	"""
	Ustvari spisek ki predstavlja vektor v 8 dimenzijskem prostoru.
	Izpiši normaliziran vektor in njegovo dolžino.
	"""
	pass


def skraliranje_vektorja():
	"""
	Mapiraj vektor tako da bo največji element 1 najmanjši pa 0.
	"""
	pass


def kot_vektorja():
	"""
	Ustvari dva spiska ki predstavljata vektorja v 8 dimenzijskem prostoru. Izračunaj kot med njima.
	"""
	pass


def Rotacija_vektorja():
	"""
	Rotiraj vektor okoli drugega vektorja.
	:return:
	"""
	pass
