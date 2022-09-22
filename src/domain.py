from typing import Callable, List
import inspect
from inspect import Parameter


class Test:
	def __init__(self, args, result):
		self.args = args
		self.result = result

	@property
	def inputs(self):
		return {'input': self.args}


class Exercise:

	def __init__(self, module, function: Callable):
		sign = inspect.signature(function)

		self.module = module
		self.function: Callable = function
		self.docs: str = ""
		self.args: List[Parameter] = list(sign.parameters.values())  # {name, annotation}
		self.return_type: Callable = sign.return_annotation
		self.tests: List[Test] = []

		self.__init()

	def __init(self):

		is_docs = True
		for i, line in enumerate(self.function.__doc__.split('\n')):
			if is_docs:
				self.docs += line + "\n"
			elif line.count(',') == len(self.args):
				infos = line.split(',')
				result = self.return_type(infos.pop(-1))
				for j, info in enumerate(infos):
					infos[j] = self.args[j].annotation(info)
				self.tests.append(Test(infos, result))

			if ':return:' in line:
				is_docs = False
		self.docs = self.docs.strip()

	@property
	def _inputs(self):
		return [test.inputs for test in self.tests]
	@property
	def _outputs(self):
		return [test.result for test in self.tests]

	def python(self):
		args_str = ", ".join([f"{arg.name}: {arg.annotation.__name__}" for arg in self.args])
		return f'''
			import python 
			
			
			def {self.function.__name__}({args_str}) -> {self.return_type.__name__}:
				"""
				{self.docs}
				"""
				
				
			if __name__ == '__main__':
				python.test({self.function.__name__})
		'''.replace("\t\t\t", "").strip() + "\n"
