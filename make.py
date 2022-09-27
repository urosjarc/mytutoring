import ast
import glob
import shutil
from pathlib import Path

from compiler.compiler import Compiler


def run(sourceDir: Path, binDir: Path):
	compiler = Compiler()
	sourceDir = sourceDir.resolve()
	binDir = binDir.resolve()
	shutil.rmtree(binDir, ignore_errors=True)

	for file in glob.iglob(f"{sourceDir}/**/*.py", recursive=True):
		innerPath = Path(file).relative_to(sourceDir)
		fileName = innerPath.stem
		with open(file) as fstart:
			module = ast.parse(fstart.read())
			for lang in Compiler.lang:
				endDir = binDir.joinpath(lang, innerPath.parent).resolve()
				endDir.mkdir(parents=True, exist_ok=True)

				source = compiler.compile(fileName, module, lang)

				with open(endDir.joinpath(f'{fileName}.{lang}'), 'w') as fend:
					fend.write(source)


if __name__ == '__main__':
	run(sourceDir=Path('client').resolve(),
	    binDir=Path('bin').resolve())
