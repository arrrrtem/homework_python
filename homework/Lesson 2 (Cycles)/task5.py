b = 0
while (a := int(input())) != 0:
    print(a - a * 0.15)
    b += (a - a * 0.15)
print(b)