from typing import Callable, List
import inspect
from inspect import Parameter
import autopep8


class Exercise:

	def __init__(self, module, function: Callable):
		sign = inspect.signature(function)

		self.module = module
		self.function: Callable = function
		self.docs: str = ""
		self.args: List[Parameter] = list(sign.parameters.values())  # {name, annotation}
		self.returns: Callable = sign.return_annotation
		self.tests = []

		self._init()

	def _init(self):

		is_docs = True
		for i, line in enumerate(self.function.__doc__.split('\n')):
			if is_docs:
				self.docs += line + "\n"
			elif line.count(',') == len(self.args):
				infos = line.split(',')
				returns = self.returns(infos.pop(-1))
				for j, info in enumerate(infos):
					infos[j] = self.args[j].annotation(info)
				self.tests.append((infos, returns))

			if ':return:' in line:
				is_docs = False

	def python(self):
		args_str = ", ".join([f"{arg.name}: {arg.annotation.__name__}" for arg in self.args])
		return autopep8.fix_code(f"""
import python
		
def {self.function.__name__}({args_str}) -> {self.returns.__name__}:
	'''{self.docs}\t'''
	
	
	return None

if __name__ == '__main__':
	python.test({self.function.__name__})
""")
