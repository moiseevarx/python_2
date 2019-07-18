import csv
import json
import yaml
import re


def get_data():
    k = 1
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    test = []
    main_data = []
    while k < 4:
        with open('info_{}.txt'.format(k), encoding='cp1251') as file:
            f_result = []
            for line in file:
                line = line.encode('utf-8').decode('utf-8')
                if re.match('Изготовитель системы', line):
                    s_result = re.split(':', line)
                    os_prod_list.append(s_result[1].strip())
                    main_data.append(s_result[0])
                    f_result.append(s_result[1].strip())
                if re.match('Название ОС', line):
                    s_result = re.split(':', line)
                    os_name_list.append(s_result[1].strip())
                    main_data.append(s_result[0])
                    f_result.append(s_result[1].strip())
                if re.match('Код продукта', line):
                    s_result = re.split(':', line)
                    os_code_list.append(s_result[1].strip())
                    main_data.append(s_result[0])
                    f_result.append(s_result[1].strip())
                if re.match('Тип системы', line):
                    s_result = re.split(':', line)
                    os_type_list.append(s_result[1].strip())
                    main_data.append(s_result[0])
                    f_result.append(s_result[1].strip())
            test.append(f_result)
        k += 1
    del main_data[4::]

    test.insert(0, main_data[0:4])

    print(test)
    return test



def write_to_csv():
    with open('data_write.csv', 'w') as f_w:
        f_w_writer = csv.writer(f_w)
        data = get_data()
        f_w_writer.writerows(data)

    # with open('data_write.csv', 'r') as f_r:
    # print(f_r.read())


write_to_csv()