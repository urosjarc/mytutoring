import shutil
import sys
from pathlib import Path
import importlib
from typing import Dict, Callable

from src.domain import Exercise
import tests
import src.clients

this = sys.modules[__name__]
root = Path(tests.__file__).parent.parent
exercises: Dict[str, Exercise] = {}
clients = []


def init():
	init_exercises()
	init_clients()


def init_exercises():
	for dir in this.root.joinpath('tests').iterdir():
		if dir.is_dir() and not dir.name.startswith('__'):
			for file in dir.iterdir():
				package = dir.name
				module = file.name.replace('.py', '')
				mod = importlib.import_module(f'tests.{package}.{module}')
				for k, v in mod.__dict__.items():
					if isinstance(v, Callable):
						this.exercises[k] = Exercise(mod, v)


def init_clients():
	for k, v in Exercise.__dict__.items():
		if not k.startswith('_'):
			this.clients.append(k)

	for client in this.clients:
		client_path = root.joinpath(client)
		shutil.rmtree(client_path, ignore_errors=True)

		test_root = Path(src.clients.__file__).parent
		client_path.mkdir(parents=True, exist_ok=True)
		shutil.copy(src=test_root.joinpath(f'{client}.py'), dst=client_path.joinpath('__init__.py'))

		for name, exercise in this.exercises.items():

			module_path = client_path.joinpath(exercise.module.__name__.replace('tests.', '').replace('.', '/'))
			module_path.parent.mkdir(parents=True, exist_ok=True)
			file_path = module_path.parent.joinpath(f'{exercise.function.__name__}.py')

			with open(file_path, 'a') as file:
				code = getattr(exercise, client)()
				file.write(code)
