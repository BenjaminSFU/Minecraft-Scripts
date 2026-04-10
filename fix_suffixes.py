from pathlib import Path as p, PurePath as pu
from os import system as sys

to_delete = []

cwd = p.cwd()
for path, subdir, files in cwd.walk():
    for file in files:
        if pu(file).suffix == '.bak':
            to_delete.append(path / file)
        else:
            oldfile = path / file
            oldfile = oldfile.resolve()
            newfile = p(pu(oldfile.parent)) / f'{pu(oldfile.stem)}.msc'
            sys(f'mv {oldfile} {newfile}')

for file in to_delete:
    file = file.resolve()
    sys(f'rm {str(file)}')