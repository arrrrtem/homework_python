"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

import queue
import threading

# Очередь для хранения фамилий студентов
students_queue = queue.Queue()

# Функция для добавления фамилий в очередь
def add_students():
    while True:
        student_name = input("Введите фамилию студента (или 'off' для завершения): ")
        if student_name.lower() == 'off':
            break
        students_queue.put(student_name)

# Функция для отчисления студентов из очереди
def dismiss_students():
    while True:
        student_name = students_queue.get()
        print(f"Студент {student_name} отчислен.")
        # Пометим, что задача выполнена
        students_queue.task_done()

# Добавляем несколько студентов в очередь
students_queue.put("Иванов")
students_queue.put("Петров")

# Запускаем функции в разных потоках
add_thread = threading.Thread(target=add_students)
dismiss_thread = threading.Thread(target=dismiss_students)

add_thread.start()
dismiss_thread.start()

# Ждем завершения ввода пользователем
add_thread.join()

# Ждем завершения отчисления студентов
students_queue.join()

# Добавляем "off" в очередь, чтобы завершить поток отчисления
students_queue.put("off")

# Ждем завершения потока отчисления
dismiss_thread.join()

print("Программа завершена.")
