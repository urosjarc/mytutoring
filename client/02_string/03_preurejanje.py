def obratna_razsporeditev(a: str):
	"""
	Obrni dano besedo narobe.
	:param a: Beseda
	:return: Obrnjeno besedo.
	>>> obratna_razsporeditev("adfzcvsdf")
	'fdsvczfda'
	>>> obratna_razsporeditev("Danes je lep dan!")
	'!nad pel ej senaD'
	"""
	return a[::-1]

def sortiraj_crke(a: str):
	"""
	Uporabnik vnese besedo.
	Sortiraj črke besede
	:param a: Beseda.
	:return: Sortirana beseda.
	>>> sortiraj_crke("adf*)afgd,er.345,<4")
	')*,,.3445<aaddeffgr'
	>>> sortiraj_crke("adG d,er.345,<4")
	' ,,.3445<Gadder'
	"""
	return ''.join(sorted(a))


def sortiraj_besede(a: str):
	"""
	Izpisi besede v stavku po slovarskem vrstnem redu.
	:param a: Stavek.
	>>> sortiraj_besede('asdf aaeb faad df,as!df addf ad.adt....fcsf,sdf acvae...sd acv   adf as f df')
	aaeb
	acv
	acvaesd
	adadtfcsfsdf
	addf
	adf
	as
	asdf
	df
	dfasdf
	f
	faad
	"""
	s = []
	for b in a.split():
		s.append(b)

	bes = []
	for b in sorted(s):
		be = ''
		for e in b:
			if e.isalpha():
				be += e
		bes.append(be)

	for b in sorted(bes):
		print(b)
