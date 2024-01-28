"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json

task = ["oleg", 24, ["Belarus", "Russia"]]

# Имя файла формируется на основе вашей фамилии и номера задания
filename = "your_lastname_task_number.json"

# Создаем словарь для сохранения в JSON
data = {
    "name": task[0],
    "age": task[1],
    "countries": task[2]
}

# Записываем данные в JSON-файл с отступом 4
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Данные сохранены в файл {filename}")
