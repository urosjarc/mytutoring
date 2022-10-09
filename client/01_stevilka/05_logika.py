import calendar


def vecje(a: int, b: int):
	"""
	Preveri ali je prva stevilka vecja od druge.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Rezultat logike.
	>>> vecje(5, 3)
	True
	>>> vecje(3,3)
	False
	>>> vecje(3, 5)
	False
	"""
	return a > b


def manjse(a: int, b: int):
	"""
	Preveri ali je prva stevilka manjsa od druge.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Rezultat logike.
	>>> manjse(5, 3)
	False
	>>> manjse(3,3)
	False
	>>> manjse(3, 5)
	True
	"""
	return a < b


def vecje_enako(a: int, b: int):
	"""
	Preveri ali je prva stevilka vecja ali enaka od druge.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Rezultat logike.
	>>> vecje_enako(5, 3)
	True
	>>> vecje_enako(3,3)
	True
	>>> vecje_enako(3, 5)
	False
	"""
	return a >= b


def manjse_enako(a: int, b: int):
	"""
	Preveri ali je prva stevilka manjsa ali enaka od druge.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Rezultat logike.
	>>> manjse_enako(5, 3)
	False
	>>> manjse_enako(3,3)
	True
	>>> manjse_enako(3, 5)
	True
	"""
	return a <= b


def enako(a: int, b: int):
	"""
	Preveri ali je prva stevilka enaka drugi.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Rezultat logike.
	>>> enako(5, 3)
	False
	>>> enako(3,3)
	True
	>>> enako(3, 5)
	False
	"""
	return a == b


def ni_enako(a: int, b: int):
	"""
	Preveri ali je prva stevilka ni enaka od druge.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Rezultat logike.
	>>> ni_enako(5, 3)
	True
	>>> ni_enako(3,3)
	False
	>>> ni_enako(3, 5)
	True
	"""
	return a != b


def vecja_stevilka(a: int, b: int):
	"""
	Vrni vecjo stevilko
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Vecja stevilka.
	>>> vecja_stevilka(3,5)
	5
	>>> vecja_stevilka(4, 3)
	4
	>>> vecja_stevilka(2,2)
	2
	"""
	return a if a > b else b


def soda(a: int):
	"""
	Izpisi ali je stevilka soda ali liha.
	:param a: Stevilka.
	:return: Da/Ne
	>>> soda(5)
	'Ne'
	>>> soda(4)
	'Da'
	"""
	return "Da" if a % 2 == 0 else "Ne"


def liha(a: int):
	"""
	Izpisi ali je stevilka liha.
	:param a: Stevilka.
	:return: Da/Ne
	>>> liha(5)
	'Da'
	>>> liha(4)
	'Ne'
	"""
	return "Ne" if a % 2 == 0 else "Da"


def deljivost(a: int, b: int):
	"""
	Izpiši, če je prva številka deljiva z drugo številko.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:return: Da/Ne
	>>> deljivost(15, 3)
	'Da'
	>>> deljivost(17, 3)
	'Ne'
	"""
	return "Da" if a % b == 0 else "Ne"


def pozitivnost(a: int):
	"""
	Povej ali je številka pozitivna, negativna ali nič.
	:param a: Stevilka.
	:return: Nic/Pozitivna/Negativna
	>>> pozitivnost(5)
	'Pozitivna'
	>>> pozitivnost(-5)
	'Negativna'
	>>> pozitivnost(0)
	'Nic'
	"""
	if a == 0:
		return 'Nic'
	elif a > 0:
		return 'Pozitivna'
	else:
		return "Negativna"


def ime_dneva(a: int):
	r"""
	Uporabnik vnese število dneva.
	Izpiši ime dneva.
	:param a: Stevilka dneva.
	:return: Ime dneva.
	>>> ' '.join([ime_dneva(i) for i in range(1, 8)])
	'Pon Tor Sre Cet Pet Sob Ned'
	"""
	return ['Pon', 'Tor', 'Sre', 'Cet', 'Pet', 'Sob', 'Ned'][a - 1]


def najvecja_stevilka(a: int, b: int, c: int):
	"""
	Uporabnik vnese tri številke.
	Izpiši največjo številko.
	:param a: Prva stevilka.
	:param b: Druga stevilka.
	:param c: Tretja stevilka.
	:return: Najvecja stevilka.
	>>> najvecja_stevilka(0,0,0)
	0
	>>> najvecja_stevilka(1,1,0)
	1
	>>> najvecja_stevilka(2,1,1)
	2
	>>> najvecja_stevilka(1,2,3)
	3
	>>> najvecja_stevilka(2,4,3)
	4
	>>> najvecja_stevilka(4,3,5)
	5
	>>> najvecja_stevilka(5,6,4)
	6
	>>> najvecja_stevilka(7,5,6)
	7
	>>> najvecja_stevilka(8,7,6)
	8
	"""
	return max(a, b, c)


def prestopno_leto(a: int):
	"""
	Uporabnik vnese leto.
	Izpiši ali je leto prestopno.
	:param a: Leto
	:return: Da/Ne
	>>> prestopno_leto(800)
	True
	>>> prestopno_leto(700)
	False
	>>> prestopno_leto(804)
	True
	>>> prestopno_leto(805)
	False
	"""
	if a % 400 == 0:
		return True
	if a % 100 == 0:
		return False
	if a % 4 == 0:
		return True
	return False


def vstop_v_klub(starost: int, vip: bool, imas_denar: bool):
	"""
	Preveri ali lahko vstopis v klub.
	:param starost: Starost cloveka.
	:param vip: Ali je VIP gost.
	:param imas_denar: Ali imas denar za vstop.
	:return: True/False
	>>> vstop_v_klub(12, False, False)
	False
	>>> vstop_v_klub(12, False, True)
	False
	>>> vstop_v_klub(12, True, False)
	True
	>>> vstop_v_klub(12, True, True)
	True
	>>> vstop_v_klub(22, False, False)
	False
	>>> vstop_v_klub(22, False, True)
	True
	>>> vstop_v_klub(22, True, False)
	True
	>>> vstop_v_klub(22, True, True)
	True
	"""
	return (starost > 18 and imas_denar) or vip


def logicna_tabela(a: bool, b: bool, c: bool):
	"""
	Ustvari logiko, za katero implementiras logicno tabelo.
	:param a: Prva odlocitev.
	:param b: Druga odlocitev.
	:param c: Tretja odlocitev.
	:return: Rezultat.

	a   b   c   return
	=================================
	F   F   F   T
	F   F   T   T
	F   T   F   T
	F   T   T   F
	T   F   F   T
	T   F   T   F
	T   T   F   T
	T   T   T   F

	>>> logicna_tabela(False,False,False)
	True
	>>> logicna_tabela(False,False,True)
	True
	>>> logicna_tabela(False,True,False)
	True
	>>> logicna_tabela(False,True,True)
	False
	>>> logicna_tabela(True,False,False)
	True
	>>> logicna_tabela(True,False,True)
	False
	>>> logicna_tabela(True,True,False)
	True
	>>> logicna_tabela(True,True,True)
	False
	"""
	if not a and not (b and c):
		return True
	else:
		return not c


def avanturisticna_igra(polnoleten: bool, avto: bool, bencin: bool, osnovna: bool, starsi):
	"""
	Ugotovi kdo te bo odpeljal domov.
	:param polnoleten:
	:param avto:
	:param osnovna:
	:param bencin:
	:return: Kdo te bo odpeljal domov.

						Si polnoleten
							 /    \
							/      \
						   /        \
					   DA /        NE\
						 /            \
						/              \
					   v                v
				   Imas avto         Si v osnovni soli
					  /\                /\
					 /  \              /  \
				 DA /    \ NE      DA /    \ NE
				   /      \          /      \
				  v        v        v        v
			Imas     Prijatelj   Starsi     Kolo
			bencin                 /|\
			 /\                   / | \
			/  \          Bogati /  |  \ Revni
		DA /    \ NE            /   |   \
		  /      \             /  Batman \
		 /        \           /     |     \
		v          v         v      v      v
	  Ferrari    AMZS       BMW Batmobil Skuter

	>>> avanturisticna_igra(True, True, True, True, '')
	'Ferrari'
	>>> avanturisticna_igra(True, True, False, True, '')
	'AMZS'
	>>> avanturisticna_igra(True, False, False, True, '')
	'Prijatelj'
	>>> avanturisticna_igra(False, False, False, True, 'Bogati')
	'BMW'
	>>> avanturisticna_igra(False, False, False, True, 'Batman')
	'Batmobil'
	>>> avanturisticna_igra(False, False, False, True, 'Revni')
	'Skuter'
	>>> avanturisticna_igra(False, False, False, False, 'Revni')
	'Kolo'
	"""
	if polnoleten:
		if avto:
			if bencin:
				return 'Ferrari'
			else:
				return 'AMZS'
		else:
			return 'Prijatelj'
	else:
		if osnovna:
			if starsi == 'Bogati':
				return 'BMW'
			elif starsi == 'Batman':
				return 'Batmobil'
			else:
				return 'Skuter'
		else:
			return 'Kolo'
