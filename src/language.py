from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict


class Module:
	def __init__(self):
		self.fileName: str = ''
		self.imports: List[str] = []
		self.docs: str = ''
		self.functions: Dict[str: str] = {}


class Language(ABC):
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
	def function(self, indent: int, name: str, args: str, docs: str):
		pass

	@abstractmethod
	def main_function(self, body: str):
		pass

	def module(self, fileName: List[str], functions: List[str], tests: List[str]) -> Module:
		pass
