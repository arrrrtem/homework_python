"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""

import json

# Чтение данных из файла character.json
with open('character.json', 'r') as file:
    data = json.load(file)

# Извлечение нужной информации
name = data.get('name', 'N/A')
homeworld = data.get('homeworld', 'N/A')
episodes = data.get('episodes', [])

# Вывод информации
print(f"Имя персонажа: {name}")
print(f"Родная планета: {homeworld}")
print("Список эпизодов:")
for episode in episodes:
    print(f"  - {episode}")
