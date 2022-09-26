import ast
from typing import List

from compiler.python import Python


class Compiler:
	lang = {'py': Python()}
	ops = {
		ast.Eq: '=='
	}

	def __init__(self):
		self.lang = None

	def compile_body(self, body: List[ast.Expr]):
		if len(body) > 0:
			docs = body[0].value
			indent = docs.col_offset
			return self.compile_docs(indent, docs.s)

	def compile_args(self, args: ast.arguments):
		string = []
		for arg in args.args:
			string.append(self.lang.args(typ=arg.annotation.id, name=arg.arg))
		return ', '.join(string)

	def compile_fun(self, fun: ast.FunctionDef):
		args = self.compile_args(fun.args)
		body = self.compile_body(fun.body)
		return self.lang.function(fun.col_offset, fun.name, args, fun.returns.id, body)

	def compile_docs(self, indent, docs):
		string = []
		for line in docs.split('\n'):
			line = line.strip()
			if line == '':
				continue
			start = line.split()[0]
			if start.startswith(':'):
				info = line.replace(':', '').split()
				typ = info[0]
				if typ == 'param':
					string.append(self.lang.docs_param(info[1], ' '.join(info[1:])))
				elif typ == 'return':
					string.append(self.lang.docs_return(' '.join(info[1:])))
				else:
					raise Exception(f"Implement: {typ} docs")
			else:
				string.append(f'{self.lang.indent(indent)}{line}')
		return self.lang.docs(indent, f'\n{self.lang.indent(indent)}'.join(string))

	def compile_module(self, module: ast.Module, ext: str) -> str:
		self.lang = Compiler.lang[ext]
		string = []
		for ele in module.body:
			if isinstance(ele, ast.FunctionDef):
				string.append(self.compile_fun(ele))
			elif isinstance(ele, ast.If):
				string.append(self.compile_main(ele))
			elif isinstance(ele, ast.Expr):
				string.append(self.compile_docs(ele.col_offset, ele.value.s))

		return ('\n' * 3).join(string)

	def compile_call_args(self, args: List[ast.Constant | ast.List]):
		string = []
		for arg in args:
			# TODO: Add more stuff here!
			if isinstance(arg, ast.List):
				string.append(self.compile_call_args(arg))
			elif isinstance(arg, ast.Constant):
				string.append(str(arg.s))

		return ', '.join(string)

	def compile_test(self, asrt: ast.Assert):
		indent = asrt.col_offset
		test = asrt.test
		operation = self.ops[type(test.ops[0])]
		fun_name = test.left.func.id
		fun_call_args = self.compile_call_args(test.left.args)
		test_value = self.compile_call_args(test.comparators)
		return self.lang.test(indent, fun_name, fun_call_args, operation, test_value)

	def compile_main(self, main_if: ast.If):
		string = []
		for ele in main_if.body:
			if isinstance(ele, ast.Assert):
				string.append(self.compile_test(ele))
		body = '\n'.join(string)
		return self.lang.main(body) + '\n'  # END line
