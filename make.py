import ast
import glob
import shutil
from pathlib import Path

from compiler.main import Compiler


def run(sourceDir: Path, binDir: Path):

	compiler = Compiler()
	sourceDir = sourceDir.resolve()
	binDir = binDir.resolve()
	shutil.rmtree(binDir, ignore_errors=True)

	for file in glob.iglob(f"{sourceDir}/**/*.py", recursive=True):

		innerPath = Path(file).relative_to(sourceDir)
		ext = innerPath.suffix[1:]
		fileName = innerPath.name

		with open(file) as fstart:
			endDir = binDir.joinpath(innerPath).resolve()
			endDir.mkdir(parents=True, exist_ok=True)

			module = ast.parse(fstart.read())
			source = compiler.compile_module(module, ext)

			with open(endDir.joinpath(fileName), 'w') as fend:
				fend.write(source)


if __name__ == '__main__':
	run(sourceDir=Path('client').resolve(),
	    binDir=Path('bin').resolve())
