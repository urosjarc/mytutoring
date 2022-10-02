from src.mapping import Mapping, mapping
from src.python import Python


class C(Python):
	map: Mapping = mapping.c

	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'#include <{imports}.h>')
		return '\n'.join(string)

	def args(self, typ: str, name: str):
		return f'{typ} {name}'

	def docs_param(self, var, info):
		return f'@param {var} {info}'

	def docs_return(self, info):
		return f'@return {info}'

	def docs(self, indent: int, docs: str) -> str:
		ind = self.indent(0)
		string = [f'{ind}/**']
		for line in docs.split('\n'):
			string.append(f'{ind} * {line.strip()}')
		string.append(f'{ind} */')
		return '\n'.join(string)

	def function(self, indent: int, name: str, args: str, docs: str):
		return_indent = self.indent(indent + 1)
		return "\n".join([
			f'{docs}',
			f'void {name}({args})' + ' {\n\n',
			'}'
		])

	def main_function(self, body):
		return '\n'.join([
			'int main(int argc, char *argv[]) {',
			f'{body}',
			'}'
		])

	def test(self, indent: int, fun_name: str, fun_call_args: str):
		return f'{self.indent(indent)}{fun_name}({fun_call_args});'
