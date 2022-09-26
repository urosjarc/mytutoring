import glob
import shutil
from pathlib import Path

root = Path(".")
langs = ['c', 'cpp', 'cs', 'java', 'js', 'py', 'swift', 'ts']

cmds = [
	'@echo off\n',
	'SET "CITO=%cd%\cito\\bin\Debug\\net6.0"',
	'set "PATH=%DOT%;%CITO%;%PATH%"'
]

binDir = Path('bin')
shutil.rmtree(binDir, ignore_errors=True)

for file in glob.iglob("clients/**/*.cs", recursive=True):
	if 'obj' in file:
		continue

	info = file.split('\\')
	dirPath = "/".join(info[:-1])
	file = info[-1]
	fileName = file.replace('.cs', '')

	cmds.append(f'\nREM {dirPath}/{fileName}')
	for lang in langs:
		binDir = Path(f'bin/{lang}/{dirPath}')
		binDir.mkdir(parents=True, exist_ok=True)
		cmds.append(f'cito -o {binDir}/{fileName}.{lang} {dirPath}/{file}')

cmds.append(f'\ntimeout /t 30')

with open('MAKE.bat', 'w') as f:
	f.write("\n".join(cmds))
