def levi_del(a: float) -> int:
	"""
	Poisci levi del od decimalke
	:param a: Decimalka.
	:return: Leva stran od pike decimalke.
	>>> float_int(123.45)
	123
	>>> float_int(54.321)
	54
	"""
	return int(a)


def desni_del(a: float) -> float:
	"""
	Poisci desni del decimalke.
	:param a: Decimalka.
	:return: Desni del decimalke.
	>>> desni_del(123.45)
	0.45
	>>> desni_del(123.54)
	0.54
	"""
	return round(a - int(a), 2)


def vsota_cifer(a: int):
	"""
	Poisci vsoto cifer v stevilki.
	:param a: Cela stevilka.
	:return: Vsota cifer stevilke.
	>>> vsota_cifer(123)
	6
	>>> vsota_cifer(23456)
	20
	"""
	return sum([int(b) for b in str(a)])


def brez_pike(a: float):
	"""
	Odstrani piko iz decimalke.
	:param a: Decimalka.
	:return: Decimalko brez pike.
	>>> brez_pike(123.456)
	123456
	>>> brez_pike(654.321)
	654321
	"""
	return int("".join([str(b) for b in str(a).replace('.', '')]))


def prestavi_piko(a: float):
	"""
	Prestavi piko na zacetek decimalke.
	:param a: Decimalka.
	:return: Decimalka z piko na zacetku.
	>>> prestavi_piko(123.45)
	0.12345
	>>> prestavi_piko(34567.8912)
	0.345678912
	"""
	return a * 10 ** (-len(str(int(a))))
