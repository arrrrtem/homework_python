a = input()
d = 0
if a == "game":
    for i in range(3):
        c = input()
        b = c
        if b == 5:
            print("Вы выиграли билет на концерт!")
            d = 1
            break
        elif c == "off":
            break
if d == 1:
    print("Повезет в следующий раз :)")