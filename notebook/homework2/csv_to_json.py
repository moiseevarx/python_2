import csv
import json


data = {}
with open('data_write.csv', 'r') as file:
    f_reader = csv.reader(file)
    f_header = next(f_reader)
    print(f_header)
    f_read = list(csv.DictReader(file, f_header))
    with open('write_csv_to_json.json', 'w', encoding='utf-8') as file_json:
        file_json.write(json.dumps(f_read, ensure_ascii=False))git