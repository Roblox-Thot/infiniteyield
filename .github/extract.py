import json
with open('source', 'r') as file: lines = file.readlines()

# Clean up the cmd list
replacements = {
    "CMDs[#CMDs + 1] = {NAME = '": '',
    "'}": '',
}

with open('version', 'r') as file:
    data = json.load(file)
    version = data['Version']

out = open("commands.md", 'w')
out.write(f'# Infinite Yield v{version}\n\n')
out.write(f'## Commands\n\n')

commands = {}
for i in range(len(lines)):
    if 'CMDs[#CMDs + 1] = {NAME = ' in lines[i]:
        command_line = lines[i]

        for old, new in replacements.items():
            command_line = command_line.replace(old, new)

        command_line = command_line.strip()
        name, desc = command_line.split('\', DESC = \'')

        if (name or desc) == "": continue

        print(f'Command Name: {name}, Description: {desc}')

        out.write(f'### {name}\n{desc}\n\n')
        commands[name] = desc

with open('commands.json', 'w') as f: json.dump(commands, f, indent=4)
out.close()
