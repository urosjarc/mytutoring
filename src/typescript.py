from src.c import C
from src.mapping import Mapping, mapping, Type


class Typescript(C):
	map: Mapping = mapping.ts

	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'let {imports} = require({imports});')
		return '\n'.join(string)

	def args(self, typ: str, name: str):
		return f'{name}: {typ}'

	def docs_param(self, var, info):
		return f'@param {var} {info}'

	def docs_return(self, info):
		return f'@return {info}'

	def function(self, indent: int, name: str, args: str, docs: str):
		return "\n".join([
			f'{docs}',
			f'function {name}({args})' + ' {\n\n',
			'}'
		])

	def main_function(self, body):
		return body

	def test(self, indent: int, fun_name: str, fun_call_args: str):
		return f'{fun_name}({fun_call_args});'
