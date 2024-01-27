summa = 0
dictation = dict(Artyom = '15', Danil = '18')
dictation.update({'Kirill': '17'})
for key, value in dictation.items():
    summa += int(value)
print('Сумма возрастов равна', summa)
#ялквмом