from typing import List

from compiler.language import Language
from compiler.mapping import Mapping, mapping, Type


class Python(Language):
	map: Mapping = mapping.py

	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'import {imports}')
		return '\n'.join(string)

	def indent(self, offset: int) -> str:
		return '\t' * offset

	def args(self, typ: str, name: str):
		return f'{name}: {typ}'

	def docs_param(self, var, info):
		return f':param {var}: {info}'

	def docs_return(self, info):
		return f':return: {info}'

	def docs(self, indent: int, docs: str) -> str:
		ind = self.indent(indent)
		return f'{ind}"""\n{docs}\n{ind}"""'

	def function(self, indent: int, name: str, args: str, returns: str, docs: str):
		fun_indent = self.indent(indent)
		return_indent = self.indent(indent + 1)
		type: Type = self.map.types[returns]
		return "\n".join([
			f'{fun_indent}def {name}({args}) -> {type.name}:',
			f'{docs}\n',
			f'{return_indent}return {type.default}'
		])

	def test(self, indent: int, fun_name: str, fun_call_args: str):
		return f'{self.indent(indent)}{fun_name}({fun_call_args})'

	def main_function(self, body):
		return '\n'.join([
			f'if __name__ == "__main__":',
			f'{body}'
		])

	def module(self, fileName: List[str], imports: List[str], module_docs: List[str], functions: List[str]):
		return ''.join(module_docs + imports + functions)
