import json

with open('read1.json') as file:
    data = json.load(file)

for section, commands in data.items():
    print(section)
    print(commands)