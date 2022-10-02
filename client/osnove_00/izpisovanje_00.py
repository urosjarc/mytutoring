def hello_world():
	"""
	Na zaslon izpisi: "Hello, world!
	>>> hello_world()
	Hello, world!
	"""
	print("Hello, world!")


def funkcija():
	r"""
	Iz funkcije izpisi in vrni besedo:
	int funkcija(int a) {\n\tint test[3] = [1,2,3];\n}
	>>> a = funkcija()
	int funkcija() {
		// \\_(0.0)_//
		int oct = 0o173;        // Octal stevilka
		int hex = 0x7b;         // Hex stevilka
		char a = 'A';           // Crka
		char b[] = "Kako si?";  // Beseda
		int c[3] = [1,2,3];     // Spisek
	}
	>>> print(a)
	'int funkcija(int a) {\n\tint test[3] = [1,2,3];\n}'
	"""
	a = 'int funkcija(int a) {\n\tint test[3] = [1,2,3];\n}'
	print(a)
	return a

def octal_hex_crka():
	"""
	Izpisi besedo sestavljeno iz hex crk: '\x07'
	Izpisi besedo sestavljeno iz okt crk: '\o07'
	:return:
	"""

def alarm():
	"""
	Na zaslon izpisi simbol za alarm: \a
	"""
	print("\a")

def backspace():
	pass
def form_feed():
	pass
def new_line():
	pass
def carriage_return():
	pass
def horizontal_tab():
	pass
def vertical_tab():
	pass
def escape_sequence():
	"""
	Izpisi besedo: Hello\0World
	:return:
	"""
