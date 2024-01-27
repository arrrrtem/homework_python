"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"
Dictionary = dict()

for i in numbers:
    Dictionary[i] = numbers.count(i)

for key, value in Dictionary.items():
    print('Ключ:', key, 'Значение:', value)