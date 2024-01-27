"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English, Japanese]
1 - [English]
"""
lists_of_languages = []
for i in range(a := int(input('Введите кол-во учеников: '))):
    while a != 0:
        language_set = set()
        for i in range(group_number := int(input('Введите кол-во учеников, знающих языки: '))):
            language = input('Введите язык: ')
            language_set.add(language)
            a -= 1
        lists_of_languages.append(language_set)
intersection_list = lists_of_languages[0]
union_list = lists_of_languages[0]
for i in range(0, len(lists_of_languages)):
    intersection_list = intersection_list & set(lists_of_languages[i])
    union_list = union_list | set(lists_of_languages[i])
print('Максимум языков, которые знают школьники:', union_list, '\nЯзыки, которые знает любой школьник:', intersection_list)