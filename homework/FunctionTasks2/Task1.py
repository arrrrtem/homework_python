"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def three_if_not_none_total(fp=None, sp=None, tp=None):
    if fp:
        print('First:', fp)
    if sp:
        print('Second:', sp)
    if tp:
        print('Third:', tp)


three_if_not_none_total(input(), input(), input())
