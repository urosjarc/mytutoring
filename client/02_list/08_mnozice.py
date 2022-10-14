from typing import List


def mnozica(s: List[int]):
	"""
	Iz spiska ustvari mnozico.
	:param s: Spisek stevil.
	:return: Mnozica stevil.
	>>> mnozica([random.randint(-3, 3) for i in range(20)])
	[0, 1, 3, -2, -3, -1]
	>>> mnozica([random.randint(-5, 5) for i in range(10)])
	[3, 4, 5, -4, -3, -1]
	"""
	return list(set(s))


def unija(m1: List[int], m2: List[int]):
	"""
	Iz dveh mnozic ustvari unijo.
	:param m1: Prva mnozica.
	:param m2: Druga mnozica.
	:return: Unija mnozic.
	>>> unija([1,2,3], [3,4,5,6])
	[1, 2, 3, 4, 5, 6]
	>>> unija([1,2,3,4], [3,4,5,6, 7, 8, 9])
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> unija([1,2,3,4], [3, 2, 1, -2, -1, 0])
	[0, 1, 2, 3, 4, -1, -2]
	"""
	return list(set(m1).union(m2))


def presek(m1: List[int], m2: List[int]):
	"""
	Ustvari presek dveh mnozic.
	:param m1: Prva mnozica.
	:param m1: Druga mnozica.
	:return: Presek mnozice.
	>>> presek([1,2,3], [3,4,5,6])
	[3]
	>>> presek([1,2,3,4], [3,4,5,6, 7, 8, 9])
	[3, 4]
	>>> presek([1,2,3,4], [3, 2, 1, -2, -1, 0])
	[1, 2, 3]
	"""
	return list(set(m1).intersection(m2))


def razlika(m1: List[int], m2: List[int]):
	"""
	Ustvari razliko dveh mnozic.
	:param m1: Prva mnozica.
	:param m1: Druga mnozica.
	:return: Presek mnozice.
	>>> razlika([1,2,3], [3,4,5,6])
	[1, 2]
	>>> razlika([1,2,3,0, 4, -8], [3,4,5,6, 7, 8, 9])
	[0, 1, 2, -8]
	>>> razlika([1,2,3,4, 5, 6], [3, 2, 1, -2, -1, 0])
	[4, 5, 6]
	"""
	return list(set(m1).difference(m2))


def simetricna_razlika(m1: List[int], m2: List[int]):
	"""
	Ustvari mnozico simetrične razlike.
	:param m1: Prva mnozica.
	:param m1: Druga mnozica.
	:return: Simetricna razlika mnozic.
	>>> simetricna_razlika([1,2,3], [3,4,5,1, 2, 6])
	[4, 5, 6]
	>>> simetricna_razlika([1,2,3,0, 5, 6, 4, -8], [3,4,5,6, 7, 8, 9])
	[0, 1, 2, 7, 8, 9, -8]
	>>> simetricna_razlika([1,2,3,4, 5, 6], [3, 2, 1, -2, -1, 0])
	[0, 4, 5, 6, -1, -2]
	"""
	return list(set(m1).symmetric_difference(m2))


def kartezični_produkt(m1: List[int], m2: List[int]):
	"""
	Izpisi pare kartezičnega produkta.
	:param m1: Prva mnozica.
	:param m2: Druga mnozica.
	>>> kartezični_produkt([1,2,3], [3,5,6,7,8])  # doctest: +NORMALIZE_WHITESPACE
	(1, 3) (1, 5) (1, 6) (1, 7) (1, 8) (2, 3) (2, 5) (2, 6) (2, 7) (2, 8) (3, 3) (3, 5) (3, 6) (3, 7) (3, 8)
	>>> kartezični_produkt([1,2], [3,5,6])  # doctest: +NORMALIZE_WHITESPACE
	(1, 3) (1, 5) (1, 6) (2, 3) (2, 5) (2, 6)
	"""
	for e1 in m1:
		for e2 in m2:
			print(f'({e1}, {e2})', end=' ')


def racun_mnozic(m1: List[int], m2: List[int], m3: List[int]):
	"""
	Izracunaj mnozico: (AuB)nC
	:param m1: Prva mnozica.
	:param m2: Druga mnozica.
	:param m3: Tretja mnozica.
	:return: Izracunano mnozico.
	>>> racun_mnozic([1,2,3], [2, 3, 4], [2, 4, 5, 6])
	[2, 4]
	>>> racun_mnozic([1,2,3, 4, 5], [0, 1, 2, 3, 4, -2], [-2, 3, 4, 5, 6])
	[3, 4, 5, -2]
	"""
	return list(set(m1).union(m2).intersection(m3))


def vien_diagram(m1: List[int], m2: List[int], m3: List[int]):
	"""
	Vrni elemente vienovega diagrama katera obmocja so prekrizana z X-om.
							m1
				+-----------------------+
				|                       |
	   +-----------------------+        |
	   |        |              |        |
	   |        |  X           |        |
	   |        |         +----|------------------+
	m2 |        |         |    |   X    |         |
	   |        +---------|----|--------+         |
	   |                  |    |                  | m3
	   +-----------------------+                  |
						  |                       |
						  +-----------------------+

	:param m1: Prva mnozica.
	:param m2: Druga mnozica.
	:param m3: Tretja mnozica.
	:return: Elementi vienovega diagrama.
	>>> vien_diagram([1,2,3,4,5], [3, 4, 5, 6], [3, 4, 7, 8, 1])
	[1, 5]
	>>> vien_diagram([-3, 8, 0, 2, 9], [-3, 0, 2], [8, 2, -3, 9])
	[0, 8, 9]
	"""
	return list(set(m1).intersection(m2).union(set(m1).intersection(m3)).difference(set(m1).intersection(m2).intersection(m3)))
