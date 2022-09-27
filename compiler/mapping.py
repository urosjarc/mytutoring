from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Type:
	name: str
	default: any


@dataclass
class Types:
	int_t: Type = Type('int', 0)
	float_t: Type = Type('float', 0)
	bool_t: Type = Type('bool', False)
	str_t: Type = Type('str', "")
	chr_t: Type = Type('chr', "")

	def __getitem__(self, item):
		return self.__dict__[f'{item}_t']


@dataclass
class Imports:
	math: List[str] = ('math',)
	random: List[str] = ('random',)
	defaults: Tuple[str] = ()

	def __getitem__(self, item):
		return self.__dict__[item]


class Mapping:
	def __init__(self, types: Types, imports: Imports):
		self.types = types
		self.imports = imports

	def __getitem__(self, item):
		return self.__dict__[item]


c_char = Type('char', '')
c_string = Type('char[]', "")
cpp_string = Type('string', "")
java_string = Type('String', "")
ts_string = cpp_string
ts_number = Type('number', 0)
ts_bool = Type('boolean', 0)

c_types = Types(str_t=c_string, chr_t=c_char)
cpp_types = Types(str_t=cpp_string, chr_t=c_char)
java_types = Types(str_t=java_string, chr_t=c_char)
ts_types = Types(int_t=ts_number, float_t=ts_number, bool_t=ts_bool, str_t=ts_string, chr_t=ts_string)

c_imports = Imports(random=['stdlib', 'time'], defaults=('stdio',))
cpp_imports = Imports(math=['cmath'], random=['cstdlib', 'ctime'], defaults=('iostream',))
java_imports = Imports(math=[], random=['java.util.Random'])
ts_imports = Imports(math=[], random=[])


class mapping:
	py = Mapping(types=Types(), imports=Imports())
	c = Mapping(types=c_types, imports=c_imports)
	java = Mapping(types=java_types, imports=java_imports)
	cpp = Mapping(types=cpp_types, imports=cpp_imports)
	ts = Mapping(types=ts_types, imports=ts_imports)
