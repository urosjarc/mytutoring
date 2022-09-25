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
		for i, line in enumerate(self.function.__doc__.replace('\t', '').split('\n')):
			if is_docs:
				self.docs += "\t" + line + "\n"
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

	def _cdocs(self, prepend: str=""):

		# DOCS
		docs_final = ""
		docs_list = self.docs.split('\n')
		for i, docs in enumerate(docs_list):
			fdocs = docs.strip().split()
			if len(fdocs) != 0:
				if fdocs[0].startswith(':param'):
					for i in range(0, 2):
						fdocs[i] = fdocs[i].replace(':', '').replace('param', '@param')
				elif fdocs[0].startswith(':return:'):
					fdocs[0] = fdocs[0].replace(':return:', '@return')

			docs_final += (prepend + " * " if i != 0 else "* ") + " ".join(fdocs) + "\n"
		return docs_final[:-1]

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

	def java(self):
		return_values = {
			'int': {"default": -1, "fromString": "Integer.parseInt(var)"},
			'float': {"default": -1, "fromString": "Float.parseFloat(var)"},
			'str': {"default": "-1", "fromString": "String.valueOf(var)"},
			'chr': {"default": '-1', "fromString": "var.charAt(0)"},
		}

		return_value = return_values.get(self.return_type.__name__, "new Object()")
		args_str = ", ".join([f"{arg.annotation.__name__} {arg.name}" for arg in self.args])
		run_args_str = ", ".join([f"{return_values[str(arg.annotation.__name__)]['fromString'].replace('var', arg.name)}" for arg in self.args])


		docs = self._cdocs("\t")
		return f'''
			public class {self.function.__name__} <
				
				/**
				 {docs}
				 */
				public static {self.return_type.__name__} run({args_str})<
					return {return_value['default']};
				>
				
				public static String wrapper(String a, String b)<
					return String.valueOf(run({run_args_str}));
				>
				
				public static void main(String[] args)<
					java.test({self.function.__name__}.class);
				>
			>	
		'''.replace("\t\t\t", "").strip().replace('<', '{').replace('>', '}') + "\n"

	def javascript(self):
		args_str = ", ".join([f"{arg.name}" for arg in self.args])

		docs = self._cdocs()
		return f"""
			<html><head><script src="../../index.js"></script><script>
			
			/**
			 {docs}
			 */
			function {self.function.__name__}({args_str})<<
				return null;	
			>>
						
			test({self.function.__name__});</script></head><body><table id="table" border="1" width="100%"></table></body></html>
		""".replace("\t\t\t", "").strip().replace('<<', '{').replace('>>', '}') + "\n"

	def c(self):
		return_values = {
					 'int': {"default": -1, "fromString": "Integer.parseInt(var)"},
					 'float': {"default": -1, "fromString": "Float.parseFloat(var)"},
					 'str': {"default": "-1", "fromString": "String.valueOf(var)"},
					 'chr': {"default": '-1', "fromString": "var.charAt(0)"},
						}

		return_value = return_values.get(self.return_type.__name__, "new Object()")
		args_str = ", ".join([f"{arg.annotation.__name__} {arg.name}" for arg in self.args])

		docs = self._cdocs("\t")
		return f'''
			#include "../../client.h"
		
			/**
			 {docs}
			 */
			{self.return_type.__name__} run({args_str})<
				return {return_value['default']};
			>
				
			int main()<
				test({self.function.__name__}.class);
			>
		'''.replace("\t\t\t", "").strip().replace('<', '{').replace('>', '}') + "\n"
