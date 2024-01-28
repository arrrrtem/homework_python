""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

# Создаем папку "task4", если она еще не существует
folder_path = 'task4'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Папка 'task4' создана")

# Записываем текст в файл "answer.txt"
file_path = os.path.join(folder_path, 'answer.txt')
text = "я выполнил задание"
with open(file_path, 'w') as file:
    file.write(text)
    print(f"Текст успешно записан в файл {file_path}")