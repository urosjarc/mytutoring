import ast
from typing import List

from src.c import C
from src.cpp import Cpp
from src.java import Java
from src.language import Module
from src.python import Python
from src.typescript import Typescript


class Compiler:
	lang = {
		'py': Python(),
		'c': C(),
		'cpp': Cpp(),
		'java': Java(),
		'ts': Typescript()
	}

	def __init__(self):
		self.lang = None

	def args(self, args: ast.arguments):
		string = []
		for arg in args.args:
			if isinstance(arg.annotation, ast.Subscript):
				id = arg.annotation.value.id
			else:
				id = arg.annotation.id
			string.append(self.lang.args(typ=id, name=arg.arg))
		return ', '.join(string)

	def function(self, fun: ast.FunctionDef):
		args = self.args(fun.args)

		docs = fun.body[0].value
		tests, out, docs = self.docs(docs.col_offset, docs.s)
		return tests, out, self.lang.function(fun.col_offset, fun.name, args, docs) + '\n'

	def docs(self, indent, docs):
		string = []
		stdout = []
		tests = []

		first_test = False
		first_param = False
		nx = self.lang.indent(indent)
		for line in docs.split('\n'):
			line = line.strip()
			if line == '':
				continue
			start = line.split()[0]
			if start.startswith(':'):
				info = line.replace(':', '').split()
				typ = info[0]
				if typ == 'param':
					if not first_param:
						first_param = True
						string.append('')
					string.append(self.lang.docs_param(info[1], ' '.join(info[1:])))
				elif typ == 'return':
					string.append(self.lang.docs_return(' '.join(info[1:])))
				else:
					raise Exception(f"Implement: {typ} docs")
			elif start.startswith('>>>'):
				first_test = True
				tests.append(line.replace('>>> ', ''))
			elif first_test:
				stdout.append(line)
			else:
				string.append(f'{nx}{line}')
		return tests, stdout, f'\t"""{docs}"""'# self.lang.docs(indent, f'\n{self.lang.indent(indent)}'.join(string))

	def compile(self, fileName: str, module: ast.Module, ext: str) -> str:
		self.lang = Compiler.lang[ext]

		functions = {}
		module_docs = []

		first_docs = False

		n1, n2, n3 = ('\n' * i for i in range(1, 4))

		for ele in module.body:
			if isinstance(ele, ast.FunctionDef):
				test, out, fun = self.function(ele)
				functions[ele.name] = (test, out, n2 + fun)
			elif isinstance(ele, ast.Expr):
				if not first_docs:
					first_docs = True
					tests, outs, docs = self.docs(ele.col_offset, ele.value.s)
					module_docs.append(docs + n2)
				else:
					raise Exception("???")
		for fName, (tests, outs, fun) in functions.items():
			yield fName, module_docs, self.lang.module(fileName, [fun], tests) + '\n'
