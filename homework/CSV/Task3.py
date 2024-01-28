"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""

import csv

subjects = [
    ['Математика', 'Иванов', 8],
    ['Литература', 'Петров', 7],
    ['Химия', 'Сидоров', 6],
    ['Физика', 'Козлов', 9],
    # Добавьте свои предметы и данные
]

filename = 'ваша_фамилия.csv'

with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Название', 'Препод', 'Любовь к предмету']
    writer = csv.writer(csvfile)

    writer.writerow(fieldnames)  # Записываем заголовки столбцов

    for subject in subjects:
        writer.writerow(subject)
