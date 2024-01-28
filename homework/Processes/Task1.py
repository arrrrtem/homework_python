"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""


import multiprocessing

def sum_even(start, end):
    result = sum(x for x in range(start, end + 1) if x % 2 == 0)
    print("Сумма четных чисел:", result)

def sum_odd(start, end):
    result = sum(x for x in range(start, end + 1) if x % 2 != 0)
    print("Сумма нечетных чисел:", result)

if __name__ == "__main__":
    start_value = 1
    end_value = 1000000

    # Запуск функций в разных процессах
    process1 = multiprocessing.Process(target=sum_even, args=(start_value, end_value))
    process2 = multiprocessing.Process(target=sum_odd, args=(start_value, end_value))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
