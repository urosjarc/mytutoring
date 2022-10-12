from math import sin
from typing import List


def soda_stevila(spisek: List[int]):
	"""
	Najdi vsa soda števila v spisku.
	:param spisek: Spisek stevil.
	:return: Spisek sodih stevil.
	>>> soda_stevila([int(sin(i)*10) for i in range(20)])
	[0, 8, -2, 6, 4, 4, 6, -2]
	>>> soda_stevila([int(sin(i)*50) for i in range(20)])
	[0, 42, 32, 20, -26, 32, -14, -48]
	"""
	a = []
	for ele in spisek:
		if ele % 2 == 0:
			a.append(ele)
	return a


def izpisi_nad_povprecjem(spisek: List[int]):
	"""
	Najdi vsa števila ki so večja od povprečja vseh števil v danem spisku.
	:param spisek: Spisek stevil.
	:return: Spisek stevil vecjih od povprecja spiska.
	>>> izpisi_nad_povprecjem([int(sin(i)*10) for i in range(20)])
	[8, 9, 1, 6, 9, 4, 4, 9, 6, 1]
	>>> izpisi_nad_povprecjem([int(sin(i)*50)+10 for i in range(20)])
	[52, 55, 17, 42, 59, 30, 31, 59, 42, 17]
	"""
	a = []
	pov = sum(spisek) / len(spisek)
	for ele in spisek:
		if ele > pov:
			a.append(ele)
	return a


def lokalni_maksimumi(spisek: List[int]):
	"""
	Najdi stevila ki so večja od svojih sosedov.
	:param spisek: Spisek stevil.
	:return: Spisek lokalnih maksimumov.
	>>> lokalni_maksimumi([int(sin(i*2)*100) for i in range(20)])
	[90, 98, 99, 91, 76, 55]
	>>> lokalni_maksimumi([int(sin(i)*100)+10 for i in range(20)])
	[100, 108, 109]
	"""
	a = []
	for i in range(0, len(spisek) - 2):
		if spisek[i] < spisek[i + 1] > spisek[i + 2]:
			a.append(spisek[i + 1])
	return a


def sekanje_z_abciso(spisek: List[int]):
	"""
	Izpisi stevila kjer se graf seka z x [abcisno] os.
	Z drugimi besedami, poisci na katerih indexih se predznak stevilke zamenja.
	:param spisek: Spisek stevil.
	:return: Index nicel.
	>>> sekanje_z_abciso([int(sin(i*2)*100) for i in range(20)])
	[2, 4, 5, 7, 8, 10, 13, 15, 16, 18]
	>>> sekanje_z_abciso([int(sin(i)*100)+10 for i in range(20)])
	[4, 7, 10, 13, 16]
	"""
	a = []
	for i in range(0, len(spisek) - 2):
		if (spisek[i] > 0 > spisek[i + 1]) or (spisek[i] < 0 < spisek[i + 1]):
			a.append(i + 1)
	return a


def unikatni_elementi(spisek: List[int]):
	"""
	Najdi vse unikatne elemente v spisku.
	>>> unikatni_elementi([int(sin(i*2)*3) for i in range(20)])
	[0, 2, -2, -1, 1]
	>>> unikatni_elementi([int(sin(i)*5)+10 for i in range(20)])
	[10, 14, 7, 6, 9, 13, 12, 8]
	"""
	a = []
	for ele in spisek:
		if ele not in a:
			a.append(ele)
	return a
