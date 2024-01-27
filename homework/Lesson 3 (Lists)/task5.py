a = list(map(int, input()))
if a[0] != 0:
    print("Нет.")
else:
    if sum(a) == (a[0] + a[-1]) / 2 * (a[-1] + 1):
        print("Да.")
    else:
        print("Нет.")
