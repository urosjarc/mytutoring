import ctypes
from ctypes import c_int, c_float, c_char
from typing import List


def velikost_spremenljivke(a: c_int, b: c_float, c: c_char):
	"""
	Izpisi velikost vhodnih spremenljivk.
	:param a: Cela stevilka.
	:param b: Decimalka.
	:param c: Crka
	>>> velikost_spremenljivke(c_int(), c_float(), c_char())
	int: 4 bytes
	float: 4 bytes
	char: 1 bytes
	"""
	print(f'int: {ctypes.sizeof(a)} bytes')
	print(f'float: {ctypes.sizeof(b)} bytes')
	print(f'char: {ctypes.sizeof(c)} bytes')


def naslov_spremenljivke(a: int):
	"""
	Ugotovi naslov spremenljivke.
	:param a: Spremenljivka.
	:return: Naslov spremenljivke v hex sistemu.
	>>> a = 0
	>>> assert hex(id(a)) == naslov_spremenljivke(a)
	"""
	return hex(id(a))


def vrednost_na_naslovu(naslov: int):
	"""
	Izpisi vrednost na naslovu pomnilnika.
	:param naslov: Naslov v pomnilniku.
	:return: Vrednost na pomnilniskem mestu.
	>>> a,b = 123, 321
	>>> vrednost_na_naslovu(id(a))
	123
	>>> vrednost_na_naslovu(id(b))
	321
	"""
	return ctypes.cast(naslov, ctypes.py_object).value


def naslov_spiska(spisek: List[int]):
	"""
	Izpisi naslov in vrednost elementov v spisku.
	:param spisek: Spisek stevil.
	>>> spisek = [8,2,6,3,7]
	>>> naslov_spiska(spisek)
	adf
	"""
	print(f'{hex(id(spisek))} -> {spisek}')
	for ele in spisek:
		print(f"{hex(id(ele))} -> {ele}")


def spisek_je_pointer():
	"""
	Definiraj spremenljivko a kot spisek predefiniranih številk.
	Izpiši...
	* a, &a[0]
	* &a[0] -> a[0], a+0 -> *(a+0)
	* &a[1] -> a[1], a+1 -> *(a+1)
	* &a[2] -> a[2], a+2 -> *(a+2)
	"""
	pass


def pointer_je_spisek():
	"""
	Definiraj pointer a z mallocom in vnesi v rezerviran prostor predefinirane številke.
	Izpiši...
	* a, &a[0]
	* &a[0] -> a[0], a+0 -> *(a+0)
	* &a[1] -> a[1], a+1 -> *(a+1)
	* &a[2] -> a[2], a+2 -> *(a+2)
	"""
	pass


def izpisi_obmocje_v_pomnilniku():
	"""
	Definiraj 5 spremenljivk z specifičnimi vrednostmi.
	Izpiši katere vrednosti se nahaja nad naslovom zadnje spremenljivke.
	"""


def pointer_pointerja():
	"""
	Definiraj spremenljivko a, shrani naslov spremenljivke v pointer b, shrani naslov spremenljivke b v pointer c,
	shrani naslov spremenljivke c v pointer d.
	Izpiši vrednost spremenljivke a z spremenljivko d.
	"""
	pass


def naslov_funkcije_in_argumentov():
	"""
	Definiraj funkcijo ki sprejme argument in vrne isti argument.
	V glavnem programu ustvari spremenljivko, izpiši kje v pomnilniku se spremenljivka nahaja.
	Nato spremenljivko pošlji v klic ustvarjene funkcije in v funkciji izpiši kje se nahaja spremenljivka v pomnilniku.
	V glavnem programu nato izpiši kje v pomnilniku se nahaja vračajoča vrednost funkcije.
	Izpiši tudi kje v pomnilniku se funkcija nahaja.
	"""
	pass


def spremeni_vrednost_spremenljivke():
	"""
	Definiraj funkcijo ki sprejme argument vrne pa nič.
	V glavnem programu definiraj spremenljivko katero vrednost spremeni v definirani funkciji.
	Preveri če se je v glavnem programu spremenljivka resnično spremenila.
	"""
	pass


def memory_leak():
	"""
	Z mallocom rezerviraj neskončno prostorov v pomnilniku in poglej v taskmanagerju kako
	se pomnilnik polne. Pri vsaki rezervaciji prostora izpiši koliko je trenutno zasedenega prostora
	v gigabayt enotah.
	Izpiši pri koliko gigabaytih zmanjka prostora na pomnilniku.
	"""
	pass


def software_hacking():
	"""
	Ustvari 2 programa. V prvem programu definiraj spremenljivko in v njo zapiši vrednost ter njen naslov, prvi program naj vsako sekundo
	izpiše vrednost spremenljivke. V drugem programu probaj spremeniti vrednost spremenljivke kjer se nahaja prva spremenljivka v prvem programu.
	"""
	pass
