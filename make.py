import glob
from pathlib import Path

root = Path(".")
langs = ['c', 'cpp', 'cs', 'java', 'js', 'py', 'swift', 'ts']

cmds = [
	'@echo off',
	'SET "CITO=%cd%\cito\\bin\Debug\\net6.0"',
	'set "PATH=%DOT%;%CITO%;%PATH%"'
]
for file in glob.iglob("client/**/*.ci", recursive=True):
	info = file.split('\\')
	dirPath = "/".join(info[:-1])
	file = info[-1]
	fileName = file.replace('.ci', '')
	for lang in langs:
		cmds.append(f'cito -o {dirPath}/{fileName}.{lang} {dirPath}/{file}')

cmds.append(f'timeout /t 30')
with open('MAKE.bat', 'w') as f:
	f.write("\n".join(cmds))
