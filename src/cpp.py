from src.c import C
from src.language import Language
from src.mapping import Mapping, mapping, Type


class Cpp(C):
	map: Mapping = mapping.cpp
