from math import sin
from typing import List


def zamenjaj_maks_min(spisek: List[int]):
	"""
	V spisku zamenjaj maksimalno številko z minimalno številko.
	>>> zamenjaj_maks_min([1,6,2,4,0])
	[1, 0, 2, 4, 6]
	>>> zamenjaj_maks_min([3,8,2,9,2,-3])
	[3, 8, 2, -3, 2, 9]
	>>> zamenjaj_maks_min([-3,-8,-2,-9,-2,-3])
	[-3, -8, -9, -2, -2, -3]
	"""
	M = max(spisek)
	m = min(spisek)
	mi = spisek.index(m)
	Mi = spisek.index(M)
	spisek[mi] = M
	spisek[Mi] = m
	return spisek


def obrni_spisek(spisek: List[int]):
	"""
	Obrni spisek tako da bo zadnja številka na prvem mestu in tako dalje.
	>>> obrni_spisek([3,8,2,9,2,-3])
	[-3, 2, 9, 2, 8, 3]
	>>> obrni_spisek([-3,-8,-2,-9,-2,-3])
	[-3, -2, -9, -2, -8, -3]
	"""
	return spisek[::-1]


def bubble_sort(spisek: List[int]):
	"""
	Sortiraj spisek po vrstnem redu.
	>>> bubble_sort([3,8,2,9,2,-3])
	[-3, 2, 2, 3, 8, 9]
	>>> bubble_sort([-3,-8,-2,-9,-2,-3])
	[-9, -8, -3, -3, -2, -2]
	"""
	return sorted(spisek)


def stevilo_pojavitev(spisek: List[int]):
	"""
	Za vsako stevilo v spisku izpisi kolikokrat se pojavi.
	>>> stevilo_pojavitev([int(sin(i*2)*3) for i in range(20)])
	-2 -> 5
	-1 -> 2
	0 -> 6
	1 -> 2
	2 -> 5
	>>> stevilo_pojavitev([int(sin(i)*5)+10 for i in range(20)])
	6 -> 3
	7 -> 2
	8 -> 2
	9 -> 2
	10 -> 3
	12 -> 2
	13 -> 2
	14 -> 4
	"""
	spisek.sort()
	uniq = sorted(list(set(spisek)))
	for u in uniq:
		print(f'{u} -> {spisek.count(u)}')
