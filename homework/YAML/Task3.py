"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""

import json
import yaml

# Загрузка информации из character.json
with open('character.json', 'r') as json_file:
    data = json.load(json_file)

# Сохранение данных в YAML файл
with open('Зернов', 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)
