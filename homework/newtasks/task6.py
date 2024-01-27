week_days = 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье'
list_days = list(week_days.split(' '))
dict_days = dict()
day = 1
for i in list_days:
        dict_days[i] = day
        day += 1
for key, value in dict_days.items():
    print(key, '--', value)