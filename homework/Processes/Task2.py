"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""


def calculate_room_area(width, length, height):
    # Расчет площади 4 стен комнаты
    wall_area = 2 * (width + length) * height
    return wall_area

def calculate_paint_consumption(area):
    # Расчет расхода краски (5 литров на 1 кв.м)
    paint_consumption = area * 5
    return paint_consumption

def write_to_file(filename, content):
    # Запись в файл
    with open(filename, 'a') as file:
        file.write(content + '\n')

if __name__ == "__main__":
    # Задаем размеры комнаты
    room_width = float(input("Введите ширину комнаты: "))
    room_length = float(input("Введите длину комнаты: "))
    room_height = float(input("Введите высоту комнаты: "))

    # Рассчитываем площадь 4 стен
    wall_area = calculate_room_area(room_width, room_length, room_height)

    # Записываем в файл площадь 4 стен
    write_to_file('room_info.txt', f'Площадь 4 стен: {wall_area} кв.м')

    # Рассчитываем расход краски
    paint_consumption = calculate_paint_consumption(wall_area)

    # Записываем в файл расход краски
    write_to_file('room_info.txt', f'Расход краски: {paint_consumption} литров')
