import ast
import glob
import shutil

from pathlib import Path
from compiler import Compiler


def run(sourceDir: Path, binDir: Path):
	compiler = Compiler()
	sourceDir = sourceDir.resolve()
	binDir = binDir.resolve()
	shutil.rmtree(binDir, ignore_errors=True)

	for file in glob.iglob(f"{sourceDir}/**/*.py", recursive=True):
		innerPath = Path(file).relative_to(sourceDir)
		fileName = innerPath.stem

		if fileName in ['__init__']:
			continue

		with open(file, encoding='utf-8') as fstart:
			module = ast.parse(fstart.read())
			for lang in Compiler.lang:
				i = 0
				endDir = binDir.joinpath(lang, innerPath.parent, fileName).resolve()
				endDir.mkdir(parents=True, exist_ok=True)
				for name, docs, text in compiler.compile(fileName, module, lang):
					print(name)
					i+=1
					with open(endDir.joinpath(f'{i:>02}_{name}.{lang}'), 'w', encoding='utf-8') as fend:
						fend.write(text)

if __name__ == '__main__':
	run(sourceDir=Path('../client').resolve(),
		binDir=Path('../bin').resolve())
