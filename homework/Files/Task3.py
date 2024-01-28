"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""

def add_line_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return

    try:
        with open(output_file, 'w') as file:
            for i, line in enumerate(lines, 1):
                file.write(f"{i}: {line}")
    except Exception as e:
        print(f"Произошла ошибка при записи файла: {e}")
        return

    print(f"Содержимое файла успешно записано в {output_file} с добавлением порядковых номеров.")

# Запрос имен файлов у пользователя
input_filename = input("Введите имя исходного файла: ")
output_filename = input("Введите имя целевого файла: ")

# Вызов функции с добавлением порядковых номеров
add_line_numbers(input_filename, output_filename)
