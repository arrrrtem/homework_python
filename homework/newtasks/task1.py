stroke = input()
l = len(stroke) + 1
if stroke[0:l//2] == stroke[:l//2]:
    print('Палиндром')
else:
    print('Не палиндром')