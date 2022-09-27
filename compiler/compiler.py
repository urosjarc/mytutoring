import ast
from typing import List

from compiler.c import C
from compiler.python import Python


class Compiler:
	lang = {
		'py': Python(),
		'c': C()
	}

	ops = {
		ast.Eq: '=='
	}

	def __init__(self):
		self.lang = None

	def compile_args(self, args: ast.arguments):
		string = []
		for arg in args.args:
			string.append(self.lang.args(typ=arg.annotation.id, name=arg.arg))
		return ', '.join(string)

	def compile_fun(self, fun: ast.FunctionDef):
		args = self.compile_args(fun.args)

		docs = fun.body[0].value
		docs = self.compile_docs(docs.col_offset, docs.s)
		return self.lang.function(fun.col_offset, fun.name, args, fun.returns.id, docs) + '\n'

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

	def compile_imports(self, aliases: List[ast.alias]):
		string = []
		for alias in aliases:
			string.append(self.lang.imports(alias.name) + '\n')
		return ''.join(string)

	def compile_module(self, module: ast.Module, ext: str) -> str:
		self.lang = Compiler.lang[ext]
		string = []
		first_import = False
		n1, n2, n3 = ('\n'*i for i in range(1,4))
		for ele in module.body:
			if isinstance(ele, ast.FunctionDef):
				string.append(n2 + self.compile_fun(ele))
			elif isinstance(ele, ast.If):
				string.append(n2 + self.compile_main(ele))
			elif isinstance(ele, ast.Expr):
				string.append(self.compile_docs(ele.col_offset, ele.value.s) + n2)
			elif isinstance(ele, ast.Import):
				if not first_import:
					first_import = True
					def_imp = self.lang.imports('defaults')
					if def_imp != '':
						def_imp += '\n'
					string.append(def_imp)
				string.append(self.compile_imports(ele.names))

		return ''.join(string)

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
