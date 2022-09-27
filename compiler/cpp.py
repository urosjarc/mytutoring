from compiler.language import Language
from compiler.mapping import Mapping, mapping, Type


class Cpp(Language):

	map: Mapping = mapping.cpp

	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'#include <{imports}>')
		return '\n'.join(string)

	def indent(self, offset: int) -> str:
		return '\t' * offset

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

	def function(self, indent: int, name: str, args: str, returns: str, docs: str):
		# fun_indent = self.indent(indent)
		return_indent = self.indent(indent + 1)
		type: Type = self.map.types[returns]
		return "\n".join([
			f'{docs}',
			f'{type.name} {name}({args})' + ' {\n',
			f'{return_indent}return {type.default};',
			'}'
		])

	def test(self, indent: int, fun_name: str, fun_call_args: str, operation: str, test_value: str):
		return f'{self.indent(indent)}assert({fun_name}({fun_call_args}) {operation} {test_value});'

	def main_function(self, body):
		return '\n'.join([
			'int main(int argc, char *argv[]) {',
			f'{body}',
			'}'
		])
		first_import = True
