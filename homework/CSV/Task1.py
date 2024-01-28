"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""

import csv

with open('Task1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['Имя']} - {row['Звание']}")
