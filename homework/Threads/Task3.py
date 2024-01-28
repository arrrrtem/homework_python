"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""

import threading
import time

def reminder_daemon():
    while True:
        time.sleep(3)
        print("Вводите быстрее")

# Создаем поток-демон с функцией reminder_daemon
reminder_thread = threading.Thread(target=reminder_daemon)
reminder_thread.daemon = True  # Устанавливаем поток в режим демона
reminder_thread.start()

# Запрашиваем ввод кода от бомбы
bomb_code = input("Введите код от бомбы: ")

# Проверяем код и выводим соответствующее сообщение
if bomb_code == "верный_код":
    print("Бомба разминирована")
else:
    print("Вы взорвались")
