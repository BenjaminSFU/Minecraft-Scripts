from pathlib import Path as p

cwd = p.cwd()
search_objects = cwd / 'search_objects'

objects = cwd / 'search_objects.txt'
objects = objects.read_text().splitlines()
script_template = (cwd / 'object.template').read_text()
for o in objects:
    script_string = script_template
    colon_split = o.split(':')
    name = colon_split[0]
    if name == 'receptionist':
        continue
    object_script = search_objects / f'{name}.msc'
    object_script.touch()
    object_script.write_text(script_string.replace('#name#', name))