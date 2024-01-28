"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""

def divisible_by_11_generator():
    for number in range(0, 101):
        if number % 11 == 0:
            yield number

# Пример использования генератора
for num in divisible_by_11_generator():
    print(num)
