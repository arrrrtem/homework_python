"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def count_imt():
    weight = int(input('Введите свой вес: '))
    height = int(input('Введите свой рост: '))
    count_result = weight // ((height/100) ** 2)
    return count_result
def process_imt():
    imt_result = count_imt()
    if imt_result < 18.5:
        print_result = 'Недостаточный вес.'
    elif imt_result >= 18.5 and imt_result < 25:
        print_result = 'ИМТ в норме.'
    else:
        print_result = 'Избыточный вес.'
    return print_result


print(process_imt())