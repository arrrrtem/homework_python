"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import sys

if len(sys.argv) != 2:
    print("Ошибка: необходимо передать имя файла в качестве параметра")
else:
    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            commands = file.readlines()
            for command in commands:
                print(f"Выполняется команда: {command.strip()}")
                # здесь можно выполнить команду, например:
                # exec(command)  # выполнить команду в файле
        print("Команды успешно выполнены")
    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except Exception as e:
        print(f"Произошла ошибка при выполнении команд: {e}")