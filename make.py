# -*- coding: windows-1250 -*-
import os
from pathlib import Path

root = Path('.')
readme = ['# Podatkovne strukture']
for dirs in sorted(root.iterdir()):
	if dirs.is_dir() and not dirs.name.startswith('.'):
		dataobject = ' '.join(dirs.name.split('_')[1:]).capitalize()
		readme.append(f'## {dataobject}')
		for markdown in sorted(dirs.iterdir()):
			capter = " ".join(markdown.name.split('_')[1:]).replace('.md', '').capitalize()
			readme.append(f' * [{capter}]({markdown})')

with open('README.md', 'w', errors='ignore') as file:
	file.write("\n".join(readme))
