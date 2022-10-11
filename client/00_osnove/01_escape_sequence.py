def U_mad_bro():
	r"""
	Izpisi smejkota [U mad bro]: % ¯\_('.")_/¯ %
	>>> U_mad_bro()
	% ¯\_('.")_/¯ %
	"""
	print("% ¯\\_('.\")_/¯ %")


def unicode_ascii_znaki():
	"""
	Izpisi besedo, ki jo predstavljajo crke zapisane v unicode, hex, octal nacinu: "\u0041 \x41 \101"
	>>> unicode_ascii_znaki()
	\u0041 \x41 \101
	"""
	print("A A A")


def alarm():
	"""
	Na zaslon izpisi simbol za alarm: \a
	Preveri ali slišiš zvok alarma.
	>>> alarm()
	\a
	"""
	print("\a")


def new_line():
	"""
	Na zaslon izpisi znake: ABC\nDEF
	Preveri če se je beseda "DEF" izpisala v novi vrstici.
	>>> new_line()
	ABC
	DEF
	"""
	print("ABC\nDEF")


def horizontal_tab(a: int, b: int, c: int, d: int, e: int, f: int):
	"""
	Na zaslon izpisi tabelo iz parametrov funkcije.
	V vsaki vrstici izpisi po dve stevili.
	>>> horizontal_tab(1,1,22,22,333,333)  # doctest: +NORMALIZE_WHITESPACE
	1   1
	22  22
	333 333
	>>> horizontal_tab(333,333,22,22,1,1) # doctest: +NORMALIZE_WHITESPACE
	333 333
	22  22
	1   1
	"""
	print(f"{a}\t{b}\n{c}\t{d}\n{e}\t{f}")
