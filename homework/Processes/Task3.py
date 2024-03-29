"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""


import multiprocessing
import time

def exchange_rate(n):
    currency = n // 75
    print(f"Можно приобрести {currency} валюты на {n} сумму денег")

def main():
    for i in range(1, 4):
        p = multiprocessing.Process(target=exchange_rate, args=(i*100,))
        p.start()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
