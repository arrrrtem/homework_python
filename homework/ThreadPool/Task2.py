"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""


import queue
import concurrent.futures

def find_divisors(number, result_queue):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    result_queue.put((number, divisors))

# Создаем очередь для хранения чисел и результата
number_queue = queue.Queue()
result_queue = queue.Queue()

# Добавляем числа в очередь
for num in range(10, 21):
    number_queue.put(num)

# Создаем пул потоков
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Запускаем функцию find_divisors в пуле для каждого числа из очереди
    futures = {executor.submit(find_divisors, num, result_queue): num for num in range(10, 21)}

    # Ждем завершения всех задач
    concurrent.futures.wait(futures)

# Получаем результат из очереди и выводим на экран
while not result_queue.empty():
    number, divisors = result_queue.get()
    print(f"Число: {number}, Делители: {divisors}")
