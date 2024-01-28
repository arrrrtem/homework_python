"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""

import queue
import concurrent.futures
import os

def process_names_file(names_file, path_queue):
    with open(names_file, 'r') as file:
        for line in file:
            name = line.strip()
            file_path = f"{name}.txt"
            path_queue.put(file_path)

def create_text_file(file_path):
    with open(file_path, 'w') as file:
        file.write("This is a sample text.")

# Путь к файлу с именами
names_file_path = "Names.txt"

# Создаем очередь для хранения путей к файлам
path_queue = queue.Queue()

# Запускаем функцию process_names_file в отдельном потоке
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(process_names_file, names_file_path, path_queue)

# Запускаем функцию create_text_file в отдельном потоке для каждого пути из очереди
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(create_text_file, path_queue.get()) for _ in range(path_queue.qsize())]

# Ждем завершения всех задач
concurrent.futures.wait(futures)
