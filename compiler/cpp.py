from compiler.c import C
from compiler.language import Language
from compiler.mapping import Mapping, mapping, Type


class Cpp(C):

	map: Mapping = mapping.cpp

	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'#include <{imports}>')
		return '\n'.join(string)
