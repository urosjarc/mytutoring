import doctest
import pkgutil

def load_tests(loader, tests, pattern):
	for importer, name, ispkg in pkgutil.walk_packages(my_module.__path__, my_module.__name__ + '.'):
		tests.addTests(doctest.DocTestSuite(name))
	return tests
