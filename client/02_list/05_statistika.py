import statistics
from typing import List


def povprecje(spisek: List[int]):
	"""
	Izracunaj povprecje stevil v spisku.
	:param spisek: Spisek stevil.
	:return: Povprecje stevil v spisku.
	>>> povprecje([2,6,3,6,2,4,-3])
	2.8571
	>>> povprecje([-2,6,3,-6,2,4,-3])
	0.5714
	"""
	return round(statistics.mean(spisek), 4)


def absolutna_napaka(spisek: List[int]):
	"""
	Izracunaj povprečno napako.
	:param spisek: Spisek stevil.
	:return: Absolutno napako stevil v spisku.
	>>> absolutna_napaka([2,6,3,6,2,4,-3])
	2.16
	>>> absolutna_napaka([-2,6,3,-6,2,4,-3])
	3.63
	"""
	mean = statistics.mean(spisek)
	return round(statistics.mean([abs(mean - ele) for ele in spisek]), 2)


def mediana(spisek: List[int]):
	"""
	Izracunaj mediano.
	:param spisek: Spisek stevil.
	:return: Mediano stevil v spisku.
	>>> mediana([2,6,3,6,2,4,-3])
	3
	>>> mediana([-2,6,3,-6,2,4,-3])
	2
	"""
	return statistics.median(spisek)


def utezeno_povprecje(spisek: List[int], utezi: List[int]):
	"""
	Izracunaj povprečje meritev.
	:param spisek: Spisek stevil.
	:return: Utezeno povprecje stevil v spisku.
	>>> utezeno_povprecje([3,2,3,4,5], [3,1, 1, 3, 2])
	3.6
	>>> utezeno_povprecje([1,-2,3,4,5, 8, -3], [3,1, 1, 3, 2, 2, 8])
	0.9
	"""
	m = 0
	s = 0
	for i in range(len(spisek)):
		m += utezi[i] * spisek[i]
		s += utezi[i]
	return round(m / s, 4)


def harmonicno_povprecje(spisek: List[int], utezi: List[int]):
	"""
	Izracunaj harmonično povprečje meritev.
	:param spisek: Spisek stevil.
	:return: Harmonicno povprecje stevil v spisku.
	>>> harmonicno_povprecje([3,2,3,4,5], [3,1, 1, 3, 2])
	3.352
	>>> harmonicno_povprecje([1,2,3,4,5, 8, 3], [3,1, 1, 3, 2, 2, 8])
	2.5316
	"""
	return round(statistics.harmonic_mean(spisek, utezi), 4)


def geometrijsko_povprecje(spisek: List[int]):
	"""
	Izracunaj geometrijsko povprečje.
	:param spisek: Spisek stevil.
	:return: Geometrijsko povprecje stevil v spisku.
	>>> geometrijsko_povprecje([2,6,3,6,2,4,3])
	3.3936
	>>> geometrijsko_povprecje([2,6,3,6,2,4,3, 2,3])
	3.1565
	"""
	return round(statistics.geometric_mean(spisek), 4)


def standardna_deviacija(spisek: List[int]):
	"""
	Izracunaj standardna deviacija in varianca številk.
	:param spisek: Spisek stevil.
	:return: Standardno deviacijo stevil v spisku.
	>>> standardna_deviacija([2,6,3,6,2,4,3])
	1.7043
	>>> standardna_deviacija([2,6,3,6,2,4,3, 2,3])
	1.5899
	"""
	return round(statistics.stdev(spisek), 4)


def standardna_varianca(spisek: List[int]):
	"""
	Izracunaj standardna deviacija in varianca številk.
	:param spisek: Spisek stevil.
	:return: Standardno variacijo stevil v spisku.
	>>> standardna_varianca([2,6,3,6,2,4,3])
	2.9048
	>>> standardna_varianca([2,6,3,6,2,4,3, 2,3])
	2.5278
	"""
	return round(statistics.variance(spisek), 4)
