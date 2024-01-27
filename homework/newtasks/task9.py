stroke_for_code = input()
stroke_for_code = list(stroke_for_code)
newlist = list()
c = str()
l = 0
for i in stroke_for_code:
    newlist.append(str(stroke_for_code.count(i))+str(i))
for i in newlist:
    l += 1
    for j in newlist[l::]:
        if i == j:
            newlist.remove(j)
for i in newlist:
    c = c + i
print(c)