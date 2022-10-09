from typing import List

from src.language import Language
from src.mapping import Mapping, mapping


class Python(Language):
	map: Mapping = mapping.py

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

	def function(self, indent: int, name: str, args: str, docs: str):
		fun_indent = self.indent(indent)
		return_indent = self.indent(indent + 1)
		return "\n".join([
			f'{fun_indent}def {name}({args}):',
			f'{docs}\n',
			f'{return_indent}pass'
		])

	def main_function(self, body):
		return '\n'.join([
			f'if __name__ == "__main__":',
			f'{body}'
		])

	def module(self, fileName: List[str], functions: List[str], tests: List[str]):
		return ''.join([f.strip() for f in functions]) + '\n\n\n' + self.main_function('\n'.join([f'\t{test}' for test in tests]))
