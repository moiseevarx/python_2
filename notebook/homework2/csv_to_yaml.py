import csv
import yaml

with open('data_write.csv', 'r', encoding='utf-8') as file:
    f_read = csv.reader(file)
    f_header = next(f_read)
    with open('write_csv_to_yaml.yaml', 'w', encoding='utf-8') as file_yaml:
        for row in f_read:
            yaml.dump([dict(zip(f_header, row))], file_yaml, allow_unicode=True)