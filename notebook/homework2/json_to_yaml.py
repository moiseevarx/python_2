import json
import yaml

data = []
with open('write_csv_to_json.json') as file_json:
    file = json.load(file_json)
    #print(file)
    data = [json.load(row) for row in file_json]
    print(data)
    with open('write_json_to_yaml.yaml', 'w', encoding='utf-8') as file_yaml:
        for row in file:
            yaml.dump(row, file_yaml, allow_unicode=True)
