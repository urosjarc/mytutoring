def aritmeticni_operatorji(a: int, b: int):
	"""
	Izpisi rezultate aritmeticnih operatorjev: vsota, minus, mnozenje, deljenje, celo stevilsko deljenje,
	mod, potenciranja.
	:param a: Leva stevilka.
	:param b: Desna stevilka.
	>>> aritmeticni_operatorji(32,5)
	Vsota: 37
	Minus: 27
	Krat: 160
	Deljenje: 6.4
	Celo deljenje: 6
	>>> aritmeticni_operatorji(22,5)
	Vsota: 27
	Minus: 17
	Krat: 110
	Deljenje: 4.4
	Celo deljenje: 4
	"""
	print(f'Vsota: {a + b}')
	print(f'Minus: {a - b}')
	print(f'Krat: {a * b}')
	print(f'Deljenje: {a / b}')
	print(f'Celo deljenje: {a //b }')

def algeberski_operatorji(a: int):
	"""

	:param a:
	:return:
	"""
	print(a % b)
	print(a ** b)
