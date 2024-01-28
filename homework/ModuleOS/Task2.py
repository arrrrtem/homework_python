"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

main_folder = "target"
if not os.path.exists(main_folder):
    os.makedirs(main_folder)
    for i in range(1, 11):
        folder_name = os.path.join(main_folder, str(i))
        os.makedirs(folder_name)
    print("Папка и подпапки успешно созданы")
else:
    print("Папка 'target' уже существует")