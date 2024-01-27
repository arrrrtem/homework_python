"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""
"""
Честно, я не поняла зачем нам здесь слово "Цвета" - его я использовала для старта первой программы.
Я понимаю, что это реализуется через kwargs, поэтому написала вторую функцию start_input_colors2, но без "Цвета" и ввода с консоли
"""
#Первый вариант решения
Dictionary = dict()
def start_input_colors(count_colors, **Dictionary):
    for i in range(count_colors):
        color = input('Введите цвет: ')
        color_hex = input('Введите HEX цвета: ')
        Dictionary[color] = color_hex
    print(f"Количество цветов: {count_colors}")
    for color, hex_color in Dictionary.items():
        print(f'{color}: {hex_color}')

if a := input("Если хотите начать, введите 'Цвета' ") == 'Цвета':
    start_input_colors(int(input('Введите количество цветов: ')))

#Второй вариант решения
def start_input_colors2(count_colors, **colors):
    print(f"Количество цветов: {count_colors}")
    for color, hex_color in colors.items():
        print(f'{color}: {hex_color}')

start_input_colors2(3, Розовый = 'ffc0cb', Желтый = 'ffff00', Красный = 'ff0000')