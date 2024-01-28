"""
Из файла info.yaml выведите имя и id Ливерпуля
"""

import yaml

# Загрузка данных из файла info.yaml
with open('info.yaml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Извлечение имени и id Ливерпуля
liverpool_info = data.get('Liverpool', {})
name = liverpool_info.get('name')
id = liverpool_info.get('id')

# Вывод результата
print(f"Имя Ливерпуля: {name}")
print(f"ID Ливерпуля: {id}")
