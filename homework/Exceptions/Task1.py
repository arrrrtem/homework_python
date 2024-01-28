"""
С помощью обработки ошибок разделить все элементы этого списка на 3.
При возникновении ошибки вывести надпись "Невозможно разделить"
"""


my_list = [1, 2, 'three', 4, 5]

for element in my_list:
    try:
        result = element / 3
        print(result)
    except (TypeError, ZeroDivisionError):
        print("Невозможно разделить")
