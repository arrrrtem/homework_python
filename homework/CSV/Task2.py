"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""

import csv

data_dict = {}

with open('Task1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = (row['Имя'], row['Фамилия'])
        grade = int(row['Оценка'])
        title = row['Звание']

        if name not in data_dict:
            data_dict[name] = {}

        data_dict[name][grade] = title

print(data_dict)
