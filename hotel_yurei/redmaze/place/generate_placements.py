from pathlib import Path as p

cwd = p.cwd()
gates_path = cwd / '..' / 'gates'
place_gates = cwd / 'place_gates.msc'

if place_gates.is_file():
    place_gates.write_text("@define Block centre_block\n@define Int[] keytemp\n@fast\n")
else:
    place_gates.touch()

class gate:
    def __init__(self, inputs):
        underscore_split = inputs.split('_')
        self.level = underscore_split[0].split('#')[-1]
        match self.level:
            case 'T':
                self.y = 66
            case 'B':
                self.y = 54
            case _:
                raise Exception(f'self.level was {self.level} instead of "T" or "B"')
        colon_split = underscore_split[1].split(':')
        try:
            int(colon_split[0][-1])
        except ValueError:
            stem = colon_split[0] + "_gate"
            self.short = True
        else:
            stem = colon_split[0]
            self.short = False
        gate = stem + ".msc"
        gatefile = gates_path / gate
        if not gatefile.is_file():
            raise FileNotFoundError
        self.url = gatefile.read_text().splitlines()[-1].lstrip('# ')
        pipe_split = colon_split[-1].split('|')
        self.deviates_in = pipe_split[-1]
        comma_split = pipe_split[0].split(',')
        self.x = int(comma_split[0])
        self.z = int(comma_split[1])
        num = ""
        for i in stem:
            if i.isdigit():
                num += i
        if len(num) == 0:
            self.num = stem
        else:
            self.num = int(num)

place_template = cwd / '..' / 'templates' / 'place.msc'
long_template = place_template.read_text()
short_place_template = cwd / '..' / 'templates' / 'place_short.msc'
short_template = short_place_template.read_text()

for i in (cwd / 'all_gates.txt').read_text().splitlines():
    g = gate(i)
    if g.deviates_in == 'x':
        lx = g.x - 1
        lz = g.z
        ux = g.x + 1
        uz = g.z
    elif g.deviates_in == 'z':
        lx = g.x
        lz = g.z - 1
        ux = g.x
        uz = g.z + 1
    if not g.short:
        filetext = long_template
    else:
        filetext = short_template
    filetext = filetext.replace('#lowerx#', str(lx))
    filetext = filetext.replace('#lowerz#', str(lz))
    filetext = filetext.replace('#lowery#', str(g.y))
    filetext = filetext.replace('#upperx#', str(ux))
    filetext = filetext.replace('#upperz#', str(uz))
    filetext = filetext.replace('#uppery#', str(g.y + 3))
    filetext = filetext.replace('#centrex#', str(g.x))
    filetext = filetext.replace('#centrez#', str(g.z))
    filetext = filetext.replace('#centrey#', str(g.y))
    filetext = filetext.replace('#script_url#', g.url)
    intext = f"\n# Gate {g.num}\n\n" + filetext
    with place_gates.open(mode='a') as file:
        print(intext, file=file)