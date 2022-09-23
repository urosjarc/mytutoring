import shutil
import sys
from pathlib import Path
import importlib
from typing import Dict, Callable

from src.domain import Exercise
import tests.clients

this = sys.modules[__name__]
root = Path(tests.__file__).parent.parent
exercises: Dict[str, Exercise] = {}
clients = {
	'python': ('python', '__init__.py', 'py'),
	'javascript': ('javascript', 'index.js', 'html'),
	'java': ('java/src', 'client.java', 'java'),
}


def init():
	init_exercises()
	init_clients()


def init_exercises():
	for dir in this.root.joinpath('tests').iterdir():
		if dir.is_dir() and not dir.name.startswith('__') and dir.name not in ['clients']:
			for file in dir.iterdir():
				package = dir.name
				module = file.name.replace('.py', '')
				mod = importlib.import_module(f'tests.{package}.{module}')
				for k, v in mod.__dict__.items():
					if isinstance(v, Callable):
						this.exercises[k] = Exercise(mod, v)


def init_clients():
	test_root = Path(tests.clients.__file__).parent

	for language, (lang_dir, lang_file, ext) in this.clients.items():
		client_dir = root.joinpath(lang_dir)
		shutil.rmtree(client_dir, ignore_errors=True)

		client_dir.mkdir(parents=True, exist_ok=True)
		shutil.copy(src=test_root.joinpath(lang_file), dst=client_dir.joinpath(lang_file))

		for name, exercise in this.exercises.items():
			module_path = client_dir.joinpath(exercise.module.__name__.replace('tests.', '').replace('.', '/'))
			module_path.mkdir(parents=True, exist_ok=True)
			file_path = module_path.joinpath(f'{exercise.function.__name__}.{ext}')

			with open(file_path, 'a') as file:
				code = getattr(exercise, language)()
				file.write(code)
