'''
8.	На вход программы подается строка чисел и число k.
 Нужно найти два числа в строке в сумме дающих k.
'''
numbers_stroke = input()
l = 0
number = int(input())
for i in numbers_stroke:
    l += 1
    for j in numbers_stroke[l::]:
        if int(i) + int(j) == number:
            print('Yes', i, '+', j)
            break
    if int(i) + int(j) == number:
        break
