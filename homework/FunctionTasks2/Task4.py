"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def calculate(*numbers):
    future_tuple = list()
    list_numbers = list()
    average_numbers = sum(numbers) / len(numbers)
    future_tuple.append(round(average_numbers, 2))
    for i in numbers:
        if i > average_numbers:
            list_numbers.append(i)
    future_tuple.append(list_numbers)
    print(tuple(future_tuple))

calculate(*[int(x) for x in input('Введите числа: ').split(', ')])