"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""

import sys
import os

if len(sys.argv) != 3:
    print("Ошибка: необходимо передать 2 аргумента")
else:
    path = sys.argv[1]
    folder_name = sys.argv[2]
    folder_path = os.path.join(path, folder_name)

    try:
        os.makedirs(folder_path)
        print(f"Папка {folder_name} успешно создана по указанному пути {path}")
    except FileExistsError:
        print(f"Ошибка: папка {folder_name} уже существует по указанному пути {path}")
    except OSError as e:
        print(f"Ошибка при создании папки: {e}")