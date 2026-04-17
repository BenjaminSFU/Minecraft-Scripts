from pathlib import Path as p

cwd = p.cwd()

file = list(cwd.glob("*.msc"))[0]

text = file.read_text()
text = text.splitlines()
print(text)
for ind, i in enumerate(text):
    if i.count("https") > 0:
        text[ind] = "   @command /script remove walk {{i.getX()}} {{i.getY()}} {{i.getZ()}} Theta"

text = "\n".join(text)
file.write_text(text)