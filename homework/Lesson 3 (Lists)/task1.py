a = []
while (name := input("Введите названия игр: ")) != "0" :
    if name in a:
        print("Такая игра уже записана")
        continue
    else:
        a.append(name)
print(a)