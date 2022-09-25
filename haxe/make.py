import shutil
from pathlib import Path

import glob

shutil.rmtree('bin', ignore_errors=True)
langs = [('py', 'python'), ('js', 'js'), ('java', 'java'), ('cpp', 'cpp')]

with open('build.hxml', 'w') as f:
	for filename in glob.iglob('**/.hx', recursive=True):

		paths = filename.split("\\")
		bin_dir = Path('bin', *paths[1:-1])
		file = paths[-1].split('.')[0]

		for ext, lang in langs:
			bin_dir.mkdir(parents=True, exist_ok=True)

			f.write("\n".join([
				f'-cp {Path(*paths[:-1])}',
				f'--dce full',
				f'-main {paths[-1].replace(".hx", "")}',
				f'-{lang} {bin_dir.joinpath(file)}.{ext}\n',
			]))

			if lang =='js':
				f.write('-lib hxnodejs\n\n')

			if lang == 'cpp':
				f.write('-D toolchain=mingw')
				continue

			f.write('--next\n\n')
