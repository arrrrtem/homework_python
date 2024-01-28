"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""

def print_temperature(degrees_list):
    for temperature in degrees_list:
        print(f"Сегодня {temperature} градусов")

# Пример использования
temperatures = [20, 25, 18, 22]
print_temperature(temperatures)
