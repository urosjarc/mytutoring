import math


def fahrenheit_celzije(a: float):
	"""
	Pretvori fahrenheit v celzije.
	:param a: Temperatura [F]
	:return: Temperatura [C]
	>>> fahrenheit_celzije(123.45)
	105.67
	>>> fahrenheit_celzije(54.321)
	36.54
	"""
	return round(a - 32 / 1.8, 2)


def celzije_fahrenheit(a: float):
	"""
	Pretvori celzije v fahrenheit .
	:param a: Temperatura [C]
	:return: Temperatura [F]
	>>> celzije_fahrenheit(105.67)
	123.45
	>>> celzije_fahrenheit(36.54)
	54.32
	"""
	return round(a + 32 / 1.8, 2)


def stopinje_radiani(a: float):
	"""
	Pretvori stopinje v radijane.
	:param a: Stopinje.
	:return: Radijani zavkrozi na 2 dec.
	>>> stopinje_radiani(123.45)
	2.15
	>>> stopinje_radiani(54.321)
	0.95
	"""
	return round(math.radians(a), 2)


def radiani_stopinje(a: float):
	"""
	Pretvori radiane v stopinje.
	:param a: Radijani.
	:return: Stopinje zavkrozi na 2 dec.
	>>> radiani_stopinje(2.15)
	123.19
	>>> radiani_stopinje(0.95)
	54.43
	"""
	return round(math.degrees(a), 2)


def sekunde_time(a: int):
	"""
	Izpisi ure, minute, sekunde v stevilki ki predstavlja vsoto sekund casa od polnoci.
	:param a: Sekund od polnoci.
	:return: "X h, Y min, Z sek"
	>>> sekunde_time(12345)
	'3 h, 25 min, 45 sek'
	>>> sekunde_time(122)
	'0 h, 2 min, 2 sek'
	>>> sekunde_time(12)
	'0 h, 0 min, 12 sek'
	"""
	h = a // 3600
	min = (a - h * 3600) // 60
	sek = a - (h * 3600 + min * 60)
	return f'{h} h, {min} min, {sek} sek'


def time_sekunde(ur: int, min: int, sek: int):
	"""
	Izpisi ure, minute, sekunde v stevilki ki predstavlja vsoto sekund casa od polnoci.
	:param a: Sekund od polnoci.
	:return: "X h, Y min, Z sek"
	>>> time_sekunde(3, 25, 45)
	12345
	>>> time_sekunde(0, 2, 2)
	122
	>>> time_sekunde(0,0,12)
	12
	"""
	return ur * 3600 + min * 60 + sek
