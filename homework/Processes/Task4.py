"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""

import threading
import time
import random


def subscription_time_checker():
    time.sleep(10)  # ждем 10 секунд
    print("Ваша подписка закончилась.")
    exit()


def guess_number_game():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Давай сыграем в игру 'угадай число'!")

    while attempts > 0:
        guess = int(input("Угадай число от 1 до 10: "))
        if guess == number_to_guess:
            print("Поздравляем, вы угадали число!")
            break
        else:
            attempts -= 1
            print(f"Неверно. Осталось попыток: {attempts}")

    if attempts == 0:
        print(f"Игра окончена. Было загадано число: {number_to_guess}")


def main():
    subscription_thread = threading.Thread(target=subscription_time_checker)
    game_thread = threading.Thread(target=guess_number_game)

    subscription_thread.start()
    game_thread.start()


if __name__ == "__main__":
    main()