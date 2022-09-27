from abc import ABC, abstractmethod
from typing import List


class Language(ABC):

	@abstractmethod
	def imports(self, name) -> str:
		pass

	@abstractmethod
	def indent(self, offset: int) -> str:
		pass

	@abstractmethod
	def args(self, typ: str, name: str):
		pass

	@abstractmethod
	def docs(self, indent: int, docs: str):
		pass

	@abstractmethod
	def function(self, indent: int, name: str, args: str, returns: str, docs: str):
		pass

	@abstractmethod
	def test(self, indent: int, fun_name: str, fun_call_args: str, operation: str, test_value: str):
		pass

	@abstractmethod
	def main_function(self, body: str):
		pass

	def module(self, fileName: List[str], imports: List[str], module_docs: List[str], functions: List[str]):
		pass
