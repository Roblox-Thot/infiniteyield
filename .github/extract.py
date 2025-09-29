with open('source', 'r') as file: lines = file.readlines()

replacements = {
    "CMDs[#CMDs + 1] = {NAME = '": '',
    "'}": '',
}

out = open("out.md", 'w')
for i in range(len(lines)):
    if 'CMDs[#CMDs + 1] = {NAME = ' in lines[i]:
        command_line = lines[i]

        for old, new in replacements.items():
            command_line = command_line.replace(old, new)

        command_line = command_line.strip()
        name, desc = command_line.split('\', DESC = \'')

        if (name or desc) == "": continue

        print(f'Command Name: {name}, Description: {desc}')

        out.write(f'## {name}\n{desc}\n\n')

out.close()

