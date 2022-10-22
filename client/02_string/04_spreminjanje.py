def zamenjaj_crke(a: str):
	"""
	V stavku spremeni vse presledke v podčrtaje.
	:param a: Stavek.
	:return: Spremenjen stavek.
	>>> zamenjaj_crke("  Danes je  lep   dan! ")
	'__Danes_je__lep___dan!_'
	>>> zamenjaj_crke("       Vceraj     ni bil dober      dan   ")
	'_______Vceraj_____ni_bil_dober______dan___'
	"""
	return a.replace(' ', '_')


def odstrani_crke(a: str):
	"""
	V stavku odstrani vse presledke.
	:param a: Stavek.
	:return: Spremenjen stavek.
	>>> odstrani_crke("  Danes je  lep   dan! ")
	'Danesjelepdan!'
	>>> zamenjaj_crke("       Vceraj     ni bil dober      dan   ")
	'_______Vceraj_____ni_bil_dober______dan___'
	"""
	return a.replace(' ', '')


def vrini_crke(a: str):
	"""
	Vrini piko pred vsemi presledki.
	:param a: Stavek.
	:return: Spremenjen stavek.
	>>> vrini_crke("  Danes je  lep   dan! ")
	'.  Danes. je.  lep.   dan!. '
	>>> vrini_crke("       Vceraj     ni bil dober      dan   ")
	'.       Vceraj.     ni. bil. dober.      dan.   '
	"""
	nb = ''
	if ' ' == a[0]:
		nb += '.'
	for i in range(len(a)):
		if a[i-1] != ' ' and a[i] == ' ':
			nb += '. '
		else:
			nb += a[i]
	return nb


def odstrani_besede(stavek: str, beseda: str):
	"""
	Odstrani vse ponovitve besede v stavku.
	:param stavek: Stavek.
	:param beseda: Beseda
	:return: Spremenjen stavek.
	>>> odstrani_besede("dober dan danes je kardanski danski", "dan")
	'dober  es je karski ski'
	>>> odstrani_besede("Danes pojdi v trgovino in kupi inoks pasto in cokolino", "in")
	'Danes pojdi v trgovo  kupi oks pasto  cokolo'
	"""
	return stavek.replace(beseda, '')


def zamenjaj_besedo(stavek: str, beseda: str, nbeseda: str):
	"""
	Zamenjaj vse ponovitve besede v stavku z novo besedo.
	:param stavek: Stavek.
	:param beseda: Beseda
	:param nbeseda: Nova beseda.
	:return: Spremenjen stavek.
	>>> zamenjaj_besedo("dober dan danes je kardanski danski", "dan", "noc")
	'dober noc noces je karnocski nocski'
	>>> zamenjaj_besedo("Danes pojdi v trgovino in kupi inoks pasto in cokolino", "in", "ali")
	'Danes pojdi v trgovalio ali kupi alioks pasto ali cokolalio'
	"""
	return stavek.replace(beseda, nbeseda)

def vrini_besedo(stavek: str, beseda: str, nbeseda: str):
	"""
	Vrini novo besedo pred besedo v stavku.
	:param stavek: Stavek.
	:param beseda: Beseda
	:param nbeseda: Nova beseda.
	:return: Spremenjen stavek.
	>>> vrini_besedo("dober dan danes je kardanski danski", "dan", "noc")
	'dober nocdan nocdanes je karnocdanski nocdanski'
	>>> vrini_besedo("Danes pojdi v trgovino in kupi inoks pasto in cokolino", "in", 'ali')
	'Danes pojdi v trgovaliino aliin kupi aliinoks pasto aliin cokolaliino'
	"""
	return stavek.replace(beseda, nbeseda + beseda)
