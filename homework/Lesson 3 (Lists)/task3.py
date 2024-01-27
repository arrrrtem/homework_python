a = list(input('Введите оценки: '))
a = ([i for i in a if i != ' '])
c = 0
for i in a:
    if i == '5':
        c += 1
print(round(c / len(a) * 100), "%", sep = '')