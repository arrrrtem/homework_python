stroke = input()
list1 = list(stroke.split(' '))
print(list1)
list2 = set(list1)
list2 = list(list2)
if list1 != list2:
    print('False')
else:
    print('True')