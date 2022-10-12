import random
from math import sin
from typing import List


def naprej(spisek: List[int]):
	"""
	Izpisi indexe in elemente spiseka po vrsti.
	:param spisek: Spisek stevil.
	>>> naprej([i for i in range(1, 11, 2)])
	0 -> 1
	1 -> 3
	2 -> 5
	3 -> 7
	4 -> 9
	>>> naprej([i for i in range(8, 0, -2)])
	0 -> 8
	1 -> 6
	2 -> 4
	3 -> 2
	"""
	for i in range(len(spisek)):
		print(f'{i} -> {spisek[i]}')


def nazaj(spisek: List[int]):
	"""
	Izpisi indexe in elemente spiseka v obratnem vrstnem redu.
	:param spisek: Spisek stevil.
	>>> nazaj([i for i in range(1, 11, 2)])
	4 -> 9
	3 -> 7
	2 -> 5
	1 -> 3
	0 -> 1
	>>> nazaj([i for i in range(8, 0, -2)])
	3 -> 2
	2 -> 4
	1 -> 6
	0 -> 8
	"""
	for i in range(len(spisek) - 1, -1, -1):
		print(f'{i} -> {spisek[i]}')


def nakljucna_stevila(spisek: List[int], seed: int, n: int):
	"""
	Izpisi index in vrednost nakljucnih stevil iz spiska.
	:param spisek: Spisek stevil.
	:param seed: Seme nakljucnosti.
	:param n: Stevilo nakljucnih stevil.
	>>> nakljucna_stevila([int(sin(i)*100) for i in range(20)], 0, 5)
	12 -> -53
	13 -> 42
	1 -> 84
	8 -> 98
	16 -> -28
	>>> nakljucna_stevila([int(sin(i)*50) for i in range(20)], 1, 7)
	4 -> -37
	18 -> -37
	2 -> 45
	8 -> 49
	3 -> 7
	15 -> 32
	14 -> 49
	"""
	random.seed(seed)
	for i in range(n):
		index = random.randint(0, len(spisek))
		print(f'{index} -> {spisek[index]}')


def soda_stevila(spisek: List[int]):
	"""
	Izpisi soda stevila v spisku.
	:param spisek: Spisek stevil.
	>>> soda_stevila([i for i in range(0, 11)]) # doctest: +NORMALIZE_WHITESPACE
	0 2 4 6 8 10
	>>> soda_stevila([int(sin(i)*100) for i in range(0, 15)]) # doctest: +NORMALIZE_WHITESPACE
	0 84 90 14 98 -54 42
	"""
	for ele in spisek:
		if ele % 2 == 0:
			print(ele, end=' ')


def proti_sredini(spisek: List[int]):
	"""
	Izpisi elemente spiska od koncev proti sredini izmenjajoce.
	Pazi da izpises tudi sredinski element!
	:param spisek: Spisek stevil.
	>>> proti_sredini([i for i in range(0, 12)])  # doctest: +NORMALIZE_WHITESPACE
	0 11 1 10 2 9 3 8 4 7 5 6
	>>> proti_sredini([i for i in range(5, 16)])  # doctest: +NORMALIZE_WHITESPACE
	5 15 6 14 7 13 8 12 9 11 10
	"""
	for i in range(0, len(spisek) // 2):
		print(spisek[i], end=' ')
		print(spisek[-i - 1], end=' ')

	if len(spisek) % 2 == 1:
		print(spisek[len(spisek) // 2])


def proti_koncem(spisek: List[int]):
	"""
	Izpisi elemente spiska od sredine proti koncema izmenjajoce.
	Pazi da izpises tudi sredinski element!
	:param spisek: Spisek stevil.
	>>> proti_koncem([i for i in range(0, 12)])  # doctest: +NORMALIZE_WHITESPACE
	5 6 4 7 3 8 2 9 1 10 0 11
	>>> proti_koncem([i for i in range(5, 16)])  # doctest: +NORMALIZE_WHITESPACE
	10 9 11 8 12 7 13 6 14 5 15
	"""
	if len(spisek) % 2 == 1:
		print(spisek[len(spisek) // 2], end=' ')
	for i in range(len(spisek) // 2 - 1, -1, -1):
		print(spisek[i], end=' ')
		print(spisek[-i - 1], end=' ')


def pari_naprej(spisek: List[int]):
	"""
	Izpisi pare stevil, ki se drzijo skupaj od zacetka proti koncu.
	:param spisek: Spisek stevil.
	>>> pari_naprej([i for i in range(0, 12)])
	0 1
	1 2
	2 3
	3 4
	4 5
	5 6
	6 7
	7 8
	8 9
	9 10
	10 11
	>>> pari_naprej([i for i in range(16, -10, -2)])
	16 14
	14 12
	12 10
	10 8
	8 6
	6 4
	4 2
	2 0
	0 -2
	-2 -4
	-4 -6
	-6 -8
	"""
	for i in range(0, len(spisek) - 1):
		print(spisek[i], spisek[i + 1])


def pari_nazaj(spisek: List[int]):
	"""
	Izpisi pare stevil, ki se drzijo skupaj od konca proti zacetku.
	:param spisek: Spisek stevil.
	>>> pari_nazaj([i for i in range(0, 12)])
	11 10
	10 9
	9 8
	8 7
	7 6
	6 5
	5 4
	4 3
	3 2
	2 1
	1 0
	>>> pari_nazaj([i for i in range(16, -9, -2)])
	-8 -6
	-6 -4
	-4 -2
	-2 0
	0 2
	2 4
	4 6
	6 8
	8 10
	10 12
	12 14
	14 16
	"""
	for i in range(len(spisek) - 1, 0, -1):
		print(spisek[i], spisek[i - 1])


def trojcki_naprej(spisek: List[int]):
	"""
	Izpisi trojcke stevil, ki se drzijo skupaj od zacetka proti koncu.
	:param spisek: Spisek stevil.
	>>> trojcki_naprej([i for i in range(0, 12)])
	0 1 2
	1 2 3
	2 3 4
	3 4 5
	4 5 6
	5 6 7
	6 7 8
	7 8 9
	8 9 10
	9 10 11
	>>> trojcki_naprej([i for i in range(16, -10, -2)])
	16 14 12
	14 12 10
	12 10 8
	10 8 6
	8 6 4
	6 4 2
	4 2 0
	2 0 -2
	0 -2 -4
	-2 -4 -6
	-4 -6 -8
	"""
	for i in range(0, len(spisek) - 2):
		print(spisek[i], spisek[i + 1], spisek[i + 2])


def trojcki_nazaj(spisek: List[int]):
	"""
	Izpisi pare stevil, ki se drzijo skupaj od konca proti zacetku.
	:param spisek: Spisek stevil.
	>>> trojcki_nazaj([i for i in range(0, 12)])
	11 10 9
	10 9 8
	9 8 7
	8 7 6
	7 6 5
	6 5 4
	5 4 3
	4 3 2
	3 2 1
	2 1 0
	>>> trojcki_nazaj([i for i in range(16, -9, -2)])
	-8 -6 -4
	-6 -4 -2
	-4 -2 0
	-2 0 2
	0 2 4
	2 4 6
	4 6 8
	6 8 10
	8 10 12
	10 12 14
	12 14 16
	"""
	for i in range(len(spisek) - 1, 1, -1):
		print(spisek[i], spisek[i - 1], spisek[i - 2])
