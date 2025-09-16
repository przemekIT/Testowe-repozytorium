import json

def json_2_csv(file: str, value1, value2, separator):
    with open(file) as json_file:
        data = json.load(json_file)

        for i in range(len(data['value'])):
            print(data['value'][i][value1], data['value'][i][value2], sep=separator)

    with open(f'{file}.csv', 'w') as file:
        for i in range(len(data['value'])):
            file.write(data['value'][i][value1] + ", " + str(data['value'][i][value2]) + "\n")

json_2_csv('ceny2024+.json', 'dtime', 'rce_pln', ', ')