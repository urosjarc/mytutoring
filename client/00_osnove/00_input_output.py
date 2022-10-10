"""
This is module docs...
"""
def hello_world():
	"""
	Na zaslon izpisi: "Hello, world!
	>>> hello_world()
	Hello, world!
	"""
	print("Hello, world!")

def returns(a: int, b: float, c: chr, d: str):
	"""
	Iz funkcije vrni stavek v katerem uporabi vse dane argumente funkcije: "Cela stevilka: {a}, Decimalka: {b}, Crka: {c}, Beseda: {d}.
	:param a: Cela stevilka.
	:param b: Decimalka.
	:param c: Crka.
	:param d: Beseda.
	>>> print(returns(5, -1.2, 'a', 'prva beseda'))
	Cela stevilka: 5, Decimalka: -1.2, Crka: a, Beseda: prva beseda.
	>>> print(returns(-10, 0.12, 'b', 'druga beseda'))
	Cela stevilka: -10, Decimalka: 0.12, Crka: b, Beseda: druga beseda.
	"""
	return f"Cela stevilka: {a}, Decimalka: {b}, Crka: {c}, Beseda: {d}."

def argumenti(a: int, b: float, c: chr, d: str):
	"""
	Izpisi stavek v katerem uporabi vse dane argumente funkcije: "Cela stevilka: {a}, Decimalka: {b}, Crka: {c}, Beseda: {d}.
	:param a: Cela stevilka.
	:param b: Decimalka.
	:param c: Crka.
	:param d: Beseda.
	>>> argumenti(5, -1.2, 'a', 'prva beseda')
	Cela stevilka: 5, Decimalka: -1.2, Crka: a, Beseda: prva beseda.
	>>> argumenti(-10, 0.12, 'b', 'druga beseda')
	Cela stevilka: -10, Decimalka: 0.12, Crka: b, Beseda: druga beseda.
	"""
	print(f"Cela stevilka: {a}, Decimalka: {b}, Crka: {c}, Beseda: {d}.")


def stdin():
	r"""
	Uporabnik bo vnesel v terminal celo stevilko, decimalko, crko in besedo.
	Iz funkcije vrni stavek v katerem uporabi vse vnesene informacije: "Cela stevilka: {a}, Decimalka: {b}, Crka: {c}, Beseda: {d}.
	>>> import io, sys
	>>> sys.stdin = io.StringIO('5\n-1.2\na\nprva beseda')
	>>> print(stdin())
	Cela stevilka: 5, Decimalka: -1.2, Crka: a, Beseda: prva beseda.
	>>> sys.stdin = io.StringIO('-10\n0.12\nb\ndruga beseda')
	>>> print(stdin())
	Cela stevilka: -10, Decimalka: 0.12, Crka: b, Beseda: druga beseda.
	"""

	a = int(input())
	b = float(input())
	c = str(input())
	d = str(input())
	return f"Cela stevilka: {a}, Decimalka: {b}, Crka: {c}, Beseda: {d}."
