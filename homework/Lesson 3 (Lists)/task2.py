a = list(input("Введите оценки без запятых: "))
print(sum([a.count('3'),a.count('4'),a.count('5')])/len(a)*100)