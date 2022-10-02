from src.c import C
from src.language import Language
from src.mapping import Mapping, mapping, Type


class Cpp(C):

	map: Mapping = mapping.cpp

	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'#include <{imports}>')
		return '\n'.join(string)
