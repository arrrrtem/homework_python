"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""

import os
import threading
import time


def replace_ids_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Заменяем "ids" на "id"
        content = content.replace("ids", "id")

        with open(file_path, 'w') as file:
            file.write(content)

        print(f"Файл {file_path} обработан")
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")


# Получаем список файлов в папке "files"
folder_path = "files"
file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, file))]

# Замеряем время выполнения программы
start_time = time.time()

# Запускаем функцию для каждого файла в отдельном потоке
threads = []
for file_path in file_list:
    thread = threading.Thread(target=replace_ids_in_file, args=(file_path,))
    thread.start()
    threads.append(thread)

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

# Выводим время выполнения
end_time = time.time()
execution_time = end_time - start_time
print(f"Программа выполнена за {execution_time:.4f} секунд")
