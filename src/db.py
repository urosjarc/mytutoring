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
	for k, v in Exercise.__dict__.items():
		if not k.startswith('_'):
			this.clients.append(k)
	read()
	make_clients()


def read():
	for dir in this.root.joinpath('tests').iterdir():
		if dir.is_dir() and not dir.name.startswith('__'):
			for file in dir.iterdir():
				package = dir.name
				module = file.name.replace('.py', '')
				mod = importlib.import_module(f'tests.{package}.{module}')
				for k, v in mod.__dict__.items():
					if isinstance(v, Callable):
						this.exercises[k] = Exercise(mod, v)


def make_clients():

	for client in this.clients:
		client_path = root.joinpath(client)
		shutil.rmtree(client_path, ignore_errors=True)
		for name, exercise in this.exercises.items():

			module_path = client_path.joinpath(exercise.module.__name__.replace('tests.', '').replace('.', '/'))
			module_path.parent.mkdir(parents=True, exist_ok=True)
			file_path = client_path.joinpath(f'{exercise.function.__name__}.py')

			with open(file_path, 'a') as file:
				code = getattr(exercise, client)()
				file.write(code)

		test_root = Path(src.clients.__file__).parent
		shutil.copy(src=test_root.joinpath(f'{client}.py'), dst=root.joinpath(f'{client}/__init__.py'))
