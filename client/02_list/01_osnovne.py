import random
from typing import List


def mali_spisek(a: int, b: int, c: int):
	"""
	Ustvari spisek stevilk.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:param c: Tretja stevilka.
	:return: Spisek stevilk.
	>>> mali_spisek(1, 2, 3)
	[1, 2, 3]
	>>> mali_spisek(3, 2, 1)
	[3, 2, 1]
	>>> mali_spisek(4, 3, 2)
	[4, 3, 2]
	"""
	return [a, b, c]


def velik_spisek(zacetek: int, konec: int, korak: int):
	"""
	Ustvari velik spisek stevil zaporedja.
	:param zacetek: Zacetna manjsa stevilka.
	:param konec: Koncna vecja stevilka.
	:param korak: Pozitivni korak zaporedja.
	:return: Spisek zaporedja
	>>> velik_spisek(0, 10, 1)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> velik_spisek(5, 15, 2)
	[5, 7, 9, 11, 13, 15]
	>>> velik_spisek(0, 30, 3)
	[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
	"""
	return [i for i in range(zacetek, konec + 1, korak)]


def nakljucni_spisek(start: int, end: int, seed: int, n: int):
	"""
	Ustvari spisek nakljucnih stevil.
	:param start: Spodnja meja.
	:param end: Zgornja meja.
	:param seed: Seme nakljucnosti.
	:param n: Stevilo nakljucnih stevil.
	>>> nakljucni_spisek(-2, 3, 0, 40)
	[1, 1, -2, 0, 2, 1, 1, 0, 1, 0, 2, -1, 2, -1, 0, -1, -2, 2, 0, 2, 3, 2, -1, 0, -2, 3, -2, 3, 0, 1, 2, -2, 0, 1, 0, 2, 3, -1, 2, 1]
	>>> nakljucni_spisek(-3, 3, 0, 20)
	[3, 0, 3, 0, -3, -1, 1, 0, 0, 3, 3, -1, 0, -1, 1, -2, 1, -2, -1, -2]
	"""
	random.seed(seed)
	return [random.randint(start, end) for i in range(n)]


def prvi_element(spisek: List[int]):
	"""
	Izpisi elemente spiska:
	* Velikost spiska.
	* Prvi element.
	* Drugi element
	* Zadnji element.
	* Predzadnji element.
	:param spisek: Spisek.

	>>> prvi_element([1,2,3,4,5])
	Velikost: 5
	Prvi: 1
	Drugi: 2
	Zadnji: 5
	Predzadnji: 4
	>>> prvi_element([5,4,3,2,1])
	Velikost: 5
	Prvi: 5
	Drugi: 4
	Zadnji: 1
	Predzadnji: 2
	"""
	print(f"Velikost: {len(spisek)}")
	print(f"Prvi: {spisek[0]}")
	print(f"Drugi: {spisek[1]}")
	print(f"Zadnji: {spisek[-1]}")
	print(f"Predzadnji: {spisek[-2]}")
