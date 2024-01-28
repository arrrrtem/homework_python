"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""


import json

task = ["oleg", 24, ["Belarus", "Russia"], (24, 1), ["Moscow", "Vladikavkaz", 'Krasnodar', "Rostov", "Nalchik"]]

# Имя файла формируется на основе вашей фамилии и номера задания
filename = "your_lastname_task_number.json"

# Создаем словарь для сохранения в JSON
data = {
    "name": task[0],
    "age": task[1],
    "countries": [
        {
            "name": task[2][0],
            "time": task[3][0],
            "cities": task[4]
        },
        {
            "name": task[2][1],
            "time": task[3][1],
            "cities": []
        }
        # Добавьте дополнительные элементы, если необходимо
    ]
}

# Записываем данные в JSON-файл с отступом 4
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Данные сохранены в файл {filename}")
