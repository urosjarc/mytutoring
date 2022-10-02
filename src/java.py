from typing import List

from src.c import C
from src.mapping import Mapping, mapping, Type


class Java(C):
	map: Mapping = mapping.java
	def imports(self, name) -> str:
		string = []
		for imports in self.map.imports[name]:
			string.append(f'import {imports};')
		return '\n'.join(string)

	def function(self, indent: int, name: str, args: str, docs: str):
		fun_indent = self.indent(indent + 1)
		return_indent = self.indent(indent + 2)
		docs = docs.replace("\n", f"\n{fun_indent}")
		return "\n".join([
			f'{fun_indent}{docs}',
			f'{fun_indent}public static void {name}({args})' + ' {\n',
			f'{return_indent}',
			f'{fun_indent}' + "}"
		])

	def test(self, indent: int, fun_name: str, fun_call_args: str):
		return f'{self.indent(indent)}{fun_name}({fun_call_args});'

	def main_function(self, body):
		n1 = self.indent(1)
		body = body.replace('\n', '\n' + n1)
		return '\n'.join([
			n1 + 'public static void main(String[] args) {',
			n1 + f'{body}',
			n1 + "}",
		])

	def module(self, fileName: List[str], imports: List[str], module_docs: List[str], functions: List[str]):
		return ''.join(
			imports +
			[module_docs[0][:-1]] +
			[f'public class {fileName} ' + '{\n'] +
			functions +
			['}']
		)
