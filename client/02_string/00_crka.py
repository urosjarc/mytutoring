def crka_v_stevilko(a: chr):
	"""
	Izpiši številsko reprezentacijo črke.
	:param a: Crka.
	:return: Ascii crka stevilke.
	>>> crka_v_stevilko('a')
	97
	>>> crka_v_stevilko('3')
	51
	>>> crka_v_stevilko(' ')
	32
	"""
	return ord(a)


def stevilka_v_crko(a: int):
	"""
	Izpiši znak ki jo predstavlja stevilka.
	:param a: Stevilka
	:return: Ascii crka stevilke.
	>>> stevilka_v_crko(123)
	'{'
	>>> stevilka_v_crko(53)
	'5'
	"""
	return chr(a)


def preveri_soglasnik(a: chr):
	"""
	Preveri ali črka predstavlja soglasnik.
	:param a: Crka
	:return: Ali je crka sograsnik.
	>>> for ele in ['a', 'e', 'i', 'o' ,'u']:
	...     assert preveri_soglasnik(ele)
	...     assert preveri_soglasnik(ele.upper())
	>>> for ele in ['.', 'b', 'c' ,'z']:
	...     assert not preveri_soglasnik(ele)
	...     assert not preveri_soglasnik(ele.upper())
	"""
	return str(a).lower() in ['a', 'e', 'i', 'o', 'u']


def preveri_crko(a: chr):
	r"""
	Vrni tip crke:
	* 0 -> specijalni znak
	* 1 -> presledek,
	* 2 -> znak.
	* 3 -> številko
	* 4 -> veliko črko
	* 5 -> majhno črko,
	:param a: Crka
	:return: Koda crke.
	>>> for c in ['\n', '\t']:
	...     assert 0 == preveri_crko(c)
	>>> for c in [' ']:
	...     assert 1 == preveri_crko(c)
	>>> for c in ['"', '/', ':', '@', '[', '`', '{', '~']:
	...     assert 2 == preveri_crko(c)
	>>> for c in ['0', '5', '9']:
	...     assert 3 == preveri_crko(c)
	>>> for c in ['A', 'M', 'Z']:
	...     assert 4 == preveri_crko(c)
	>>> for c in ['a', 'm', 'z']:
	...     assert 5 == preveri_crko(c)
	"""
	s = ord(a)
	if 0 <= s <= 31:
		return 0
	elif 32 == s:
		return 1
	elif 48 <= s <= 57:
		return 3
	elif 65 <= s <= 90:
		return 4
	elif 97 <= s <= 122:
		return 5
	else:
		return 2

def velika_zacetnica(a: chr):
	"""
	Vrni veliko začetnico izbrane črke.
	:param a: Crka
	:return: Veliko zacetnico.
	>>> velika_zacetnica('a')
	'A'
	>>> velika_zacetnica('Z')
	'Z'
	>>> velika_zacetnica('A')
	'A'
	>>> velika_zacetnica('{')
	'{'
	"""
	if 97 <= ord(a) <= 122:
		return chr(ord(a) - 32)
	return a
