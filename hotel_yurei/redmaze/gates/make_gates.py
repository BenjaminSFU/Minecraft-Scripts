from pathlib import Path as p, PurePath as pu

cwd = p.cwd()
gate_template = cwd / '..' / 'templates' / 'gate.msc'
gate_template = gate_template.read_text()

for i in range(1, 23):
    gate_text = gate_template
    gate_text = gate_text.replace('#num#', str(i))
    gate_file = cwd / f'gate{i}.msc'
    gate_file.touch()
    gate_file.write_text(gate_text)