import math


def nahajanje_v_besedi(a: str):
	r"""
	Prestej presledke, ki se nahajajo v besedi.
	:param a: Beseda z presledki.
	:return: Stevilo presledkov.
	>>> nahajanje_v_besedi("ad adfs f sdf ad fsd sdfsdf    sdf sf sf")
	12
	>>> nahajanje_v_besedi("ad  fsd sdfsdf    sdf sf sf")
	9
	"""
	return a.count(' ')


def stevilo_crk(a: str):
	"""
	Izpiši število črk v besedi.
	:param a: Beseda z crkami.
	:return: Stevilo crk.
	>>> stevilo_crk("adf ,.23")
	3
	>>> stevilo_crk("adf ,.23 adf 3rlk madf")
	13
	"""
	return len([c for c in a if c.isalpha()])


def stevilo_besed(a: str):
	"""
	Izpiši število besed v stavku.
	:param a: Beseda.
	:return: Stevilo besed.
	>>> stevilo_besed(" ad     adfs    f  sdf    ad fsd sdfsdfsdf sf sf")
	9
	>>> stevilo_besed("      ad  fsd sdfsdf    sdf sf sf")
	6
	"""
	return len(a.split())


def stevilo_povedi(a: str):
	"""
	Uporabnik vnese stavek.
	Izpiši število povedi v stavku.
	:param a: Beseda.
	:return: Stevilo povedi.
	>>> stevilo_povedi("Danes je lep dan!? Kako si danes??? Dobro sem!")
	9
	>>> stevilo_povedi("Danes je lep dan!? Kako si danes??? Kako si     danes ?  Dobro sem  !")
	6
	"""
	pass


def besede(a: str):
	"""
	Uporabnik vnese stavek.
	Izpiši besede v vsaki svoji vrstici.
	:param a: Stavek z besedami.
	>>> besede("??Danes ,.je. ..   lep dAn! Kako ,.je, daNES???")
	Danes
	je
	lep
	dAn
	Kako
	je
	daNES
	"""
	for b in a.split():
		flag = False
		for c in b:
			if c.isalpha():
				flag = True
				print(c, end='')
		if flag:
			print()


def stevilo_vrstic(a: str):
	r"""
	Preštej koliko vrstic se nahaja v stavku.
	:param a: Stavek.
	:return: Število vrstic.
	>>> stevilo_vrstic("asdf as\nd asdfa\nsdf sf as f sd\nf asdfsdf s\nd asdf")
	4
	>>> stevilo_vrstic("asdf as\nd asdfasdf sf \nf asdfsdf s\nd asdf")
	3
	"""
	return a.count('\n')


def stevilo_ponovitev(stavek: str, beseda: str):
	"""
	Prestej kolikokrat se podana beseda ponovi v stavku.
	:param stavek: Stavek.
	:param beseda: Beseda.
	:return: Stevilo ponovitev.
	>>> stevilo_ponovitev("ad asdf dfasdf asfasdf df sdf asf s fdf", 'as')
	5
	>>> stevilo_ponovitev("ad asdf dfasdf asfasdf df sdf asadfaddasdfasdfasf s fdf", 'df')
	10
	>>> stevilo_ponovitev("ad asdf dfasdf asfasdf df sdf asadfaddasdfasdfasf s fdf", 'ad')
	3
	"""
	return stavek.count(beseda)


def najpogostejsa_beseda(a: str):
	"""
	Izpisi najpogostejso besedo in koliko krat se beseda ponovi v stavku.
	:param a: Stavek.
	>>> najpogostejsa_beseda("danes je lep dan, ja res je ja!")
	je -> 2
	>>> najpogostejsa_beseda("res danes res je res res lep dan, to je res")
	res -> 5
	>>> najpogostejsa_beseda("to to adf to asf sdfto to adf toro")
	to -> 6
	"""
	m = ""
	c = 0
	for b in a.split():
		st_p = a.count(b)
		if c < st_p:
			m = b
			c = st_p
	print(f'{m} -> {c}')


def oddaljenost_besed(a: str, b: str):
	r"""
	Izračunaj dolžino vektorske razlike besed.
	:param a: Prva beseda.
	:param b: Druga beseda.
	>>> oddaljenost_besed("adf", "bcd")
	4
	>>> oddaljenost_besed("bcd", "adf")
	4
	>>> oddaljenost_besed("adf", "bcdasd")
	316
	>>> oddaljenost_besed("ad.2\nf", "bc\bda\asd.?23")
	697
	"""
	i = 0
	v = 0
	while True:

		if i < len(a):
			e1 = ord(a[i])
		else:
			e1 = 0

		if i < len(b):
			e2 = ord(b[i])
		else:
			e2 = 0

		if e2 == 0 and e1 == 0:
			break

		v += abs(e2 - e1)
		i += 1

	return v


def fuzzy_search(stavek: str, beseda: str):
	"""
	Izpisi s katero besedo se v stavku beseda najbolj ujema z iskano beseda.
	:param stavek: Stavek.
	:param beseda: Beseda.
	:return: Ujemajoca beseda.
	>>> fuzzy_search("adf d adf sdf adfasdf asdf", "hello")
	'asdf'
	>>> fuzzy_search("adf d23 sdf 23 adf sdf aa244dfasdf asdf", "134abc")
	'd23'
	>>> fuzzy_search("adf d23 sdf 23 adf sdf aa244dfasdf asdf", "heheadfasdf")
	'aa244dfasdf'
	"""
	M = math.inf
	matchw = ""
	for b in stavek.split():
		dist = oddaljenost_besed(b, beseda)
		if dist < M:
			matchw = b
			M = dist
	return matchw
