from typing import List
import math
import random

random.seed(0)


def dodaj_stevilo(s: List[int], a: int):
	"""
	Dodaj stevilo na konec spiska.
	:param s: Spisek.
	:param a: Stevilo.
	:return: Novi spisek.
	>>> dodaj_stevilo([1,2,3], 0)
	[1, 2, 3, 0]
	>>> dodaj_stevilo([1,2,3, -2, 5], -1)
	[1, 2, 3, -2, 5, -1]
	>>> dodaj_stevilo([], -1)
	[-1]
	"""
	return s + [a]


def zdruzi_spiska(s1: List[int], s2: List[int]):
	"""
	Zdruzi spiska skupaj.
	:param s1: Prvi spisek.
	:param s2: Drugi spisek.
	:return: Zdruzen spisek.
	>>> zdruzi_spiska([1,2,3], [3, 5, 6, -2])
	[1, 2, 3, 3, 5, 6, -2]
	>>> zdruzi_spiska([-2,3, 8, 0], [5, 6, -2])
	[-2, 3, 8, 0, 5, 6, -2]
	>>> zdruzi_spiska([], [5, 6, -2])
	[5, 6, -2]
	"""
	return s1 + s2


def vrini_stevilo(s: List[int], i: int, a: int):
	"""
	Vrini stevilo v spisek na specificno mesto.
	:param s: Spisek stevil.
	:param i: Index mesta
	:param a: Stevilo.
	:return: Novi spisek v katerega si vrinil stevilo.
	>>> vrini_stevilo([1,2,-3,4,-5], 0, 5)
	[5, 1, 2, -3, 4, -5]
	>>> vrini_stevilo([1,2,-3,4,5, 4, 3, 2], 3, 5)
	[1, 2, -3, 5, 4, 5, 4, 3, 2]
	>>> vrini_stevilo([1,-2,3,-4,5], 5, 0)
	[1, -2, 3, -4, 5, 0]
	"""
	s.insert(i, a)
	return s


def odstrani_soda_stevila(s: List[int]):
	"""
	Ustvari spisek števil.
	Odstrani soda števila iz spiska.
	Izpiši novi spisek.
	:param s: Spisek.
	:return: Spisek brez sodih stevil.
	>>> odstrani_soda_stevila([1,2,3,4,5])
	[1, 3, 5]
	>>> odstrani_soda_stevila([1,-2,3,4,5, 9, 120, 111, 55, 50])
	[1, 3, 5, 9, 111, 55]
	"""
	return [ele for ele in s if ele % 2 == 1]

def odstrani_izjeme(s: List[int]):
	"""
	Odstrani 1/3 vseh stevil ki so najbolj oddaljena od povprecja stevil v spisku.
	:param s: Spisek stevil.
	:return: Novi spisek brez izjem.
	>>> odstrani_izjeme([int(math.sin(i)*100) for i in range(1, 10)])
	[84, 90, 14, -27, 65, 41]
	>>> odstrani_izjeme([int(math.sin(i)*50) for i in range(1, 20)])
	[42, 7, -37, -13, 32, 20, -27, -26, 21, 32, -14, -37, 7]
	"""
	a = sum(s) / len(s)
	ad = [abs(ele - a) for ele in s]
	for i in range(len(s) // 3):
		ad_max = max(ad)
		ad_maxi = ad.index(ad_max)
		ad.pop(ad_maxi)
		s.pop(ad_maxi)
	return s
