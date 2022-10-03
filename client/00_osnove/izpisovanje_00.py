def hello_world():
	"""
	Na zaslon izpisi: "Hello, world!
	>>> hello_world()
	Hello, world!
	"""
	print("Hello, world!")


def escape_sequence():
	r"""
	Izpisi smejkota [U mad bro]: ¯\_('.")_/¯
	>>> escape_sequence()
	¯\_('.")_/¯
	"""
	print("¯\\_('.\")_/¯")


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


def backspace():
	"""
	Na zaslon izpisi znake: ABC\b
	Preveri če se je znak 'C' izbrisal.
	>>> backspace()
	ABC\b
	"""
	print("ABC\b")


def new_line():
	"""
	Na zaslon izpisi znake: ABC\nDEF
	Preveri če se je beseda "DEF" izpisala v novi vrstici.
	>>> new_line()
	ABC
	DEF
	"""
	print("ABC\nDEF")


def carriage_return():
	"""
	Na zaslon izpisi znake: Hello, world!\rHello!
	Preveri če se izpisala samo beseda: "Hello!"
	>>> carriage_return()
	Hello!
	"""
	print("Hello!")


def horizontal_tab():
	"""
	Na zaslon izpisi tabelo v lepi obliki: 1\t1\n22\t22\n333\t333
	>>> horizontal_tab()
	1   1
	22  22
	333 333
	"""
	print("1\t1\n22\t22\n333\t333")
