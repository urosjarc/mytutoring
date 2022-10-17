def v_tip(a: str):
	"""
	Izpiši ali se v besedi nahaja...
	* int
	* float
	* boolean
	Pretvori besedo v pravo obliko.
	:param a: Stevilka kot beseda.
	:return: Vrednost elementa v besedi.
	>>> v_tip("123")
	123
	>>> v_tip("123.23")
	123.23
	>>> v_tip("true")
	True
	"""
	if '.' in a:
		return float(a)
	elif 'rue' in a:
		return bool(a)
	else:
		return int(a)

def v_int(a: str):
	"""
	Izpiši ali se v besedi nahaja...
	* binary
	* octal
	* hex
	* decimal
	Pretvori besedo v int obliko.
	:param a: Stevilka kot beseda.
	:return: Decimalna reprezentacija stevilke v besedi.
	>>> v_int("0xff")
	255
	>>> v_int("0xff0ab")
	1044651
	>>> v_int("0o1342")
	738
	>>> v_int("0o135142")
	47714
	>>> v_int("0b10101")
	21
	>>> v_int("0b1011101")
	93
	>>> v_int("982")
	982
	>>> v_int("12")
	12
	"""
	if '0x' in a:
		return int(a, 16)
	elif '0b' in a:
		return int(a, 2)
	elif '0o' in a:
		return int(a, 8)
	else:
		return int(a)

def velikost_decimalke(a: str):
	"""
	Ugotovi koliko številk se nahaja v decimalki
	:param a: Decimalna stevilka kot beseda.
	:return: Velikost decimalnega stevila.
	>>> velikost_decimalke('12.2333324')
	7
	>>> velikost_decimalke('1223.33324')
	5
	"""
	return len(a.split('.')[-1])

def stevilke(a: str):
	"""
	Izračunaj vsoto stevil v poljubnem stavku.
	:param a: Stavek
	:return: Vsota stevilk v stavku.
	>>> stevilke("Da3nes 23 je234 lep235 235dan2353")
	50
	>>> stevilke("..,2, 5, 9, 92, adf2334adf")
	39
	"""
	v = 0
	for c in a:
		if c.isnumeric():
			v += int(c)
	return v
