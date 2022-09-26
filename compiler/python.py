from compiler.language import Language


class Python(Language):

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

	def function(self, indent: int, name: str, args: str, returns: str, body: str):
		fun_indent = self.indent(indent)
		return_indent = self.indent(indent + 1)
		return "\n".join([
			f'{fun_indent}def {name}({args}) -> {returns}:',
			f'{body}\n',
			f'{return_indent}return {self.default_value(returns)}'
		])

	def test(self, indent: int, fun_name: str, fun_call_args: str, operation: str, test_value: str):
		return f'{self.indent(indent)}assert {fun_name}({fun_call_args}) {operation} {test_value}'

	def default_value(self, typ):
		return {
			'int': 0,
			'float': 0,
			'bool': False,
			'str': ''
		}.get(typ, None)

	def main(self, body):
		return '\n'.join([
			f'if __name__ == "__main__":',
			f'{body}'
		])
