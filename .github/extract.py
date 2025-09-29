lines = ''
with open('source', 'r') as file:
    lines = file.readlines()

replacements = {
    "CMDs[#CMDs + 1] = {NAME = '": '',
    "'}": ''
}

out = open("commands.md", 'w')
out.write('# Commands\n\n')
for i in range(len(lines)):
    if 'CMDs[#CMDs + 1] = {NAME = ' in lines[i]:
        testline = lines[i]
        for old, new in replacements.items():
            testline = testline.replace(old, new)
        testline = testline.strip()
        name, desc = testline.split('\', DESC = \'')
        if (name or desc) == "": continue
        print(f'Command Name: {name}, Description: {desc}')
        out.write(f'## {name}\n{desc}\n\n')

out.close()

