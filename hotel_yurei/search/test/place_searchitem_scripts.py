from pathlib import Path as p

cwd = p.cwd()
search_objects = cwd / 'search_objects'
test_objects = (cwd / 'test_objects.txt').read_text().splitlines()
script_text = ""
for i in search_objects.iterdir():
    name = i.stem
    url = i.read_text().splitlines()[-1].lstrip('# ')
    for o in test_objects:
        if o.split(":")[0] == name:
            corr_obj = o.split(":")[1].lstrip(' ').split(' ')
    if len(corr_obj) == 1:
        script_text += f"@bypass /s i e {corr_obj[0]} {url}\n"
    elif len(corr_obj) == 4:
        script_text += f"@bypass /s i i {corr_obj[0]} {corr_obj[1]} {corr_obj[2]} {corr_obj[3]} {url}\n"

place_searchitem_scripts = cwd / "place_searchitem_scripts.msc"
place_searchitem_scripts.touch()
place_searchitem_scripts.write_text(script_text)