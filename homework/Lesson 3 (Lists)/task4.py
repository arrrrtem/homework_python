a = []
a1 = []
c = 0
for i in range(3):
    if c == 0:
        d = 'Введите свою фамилию: '
    elif c == 1:
        d = 'Введите свою должность: '
    else:
        d = 'Введите количество человек в группе: '
        b = input(d)
        b = b.split(',')
        a1.append(list(b))
        a.extend(a1)
        break
    b = input(d)
    a.append(b)
    c += 1
print(a)