from pathlib import Path

root = Path('../docs')
readme = ['# Podatkovne strukture']
for dirs in sorted(root.iterdir()):
	if dirs.is_dir() and not dirs.name.startswith('.'):
		dataobject = ' '.join(dirs.name.split('_')[1:]).capitalize()
		readme.append(f'## {dataobject}')
		for markdown in sorted(dirs.iterdir()):
			capter = " ".join(markdown.name.split('_')[1:]).replace('.md', '').capitalize()
			relativePath = str(markdown).replace("\\", "/")
			readme.append(f' * [{capter}]({relativePath})')

with open('../README.md', 'w', errors='ignore') as file:
	file.write("\n".join(readme))
