"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
Numbers = dict()
for i in range(1, 11):
    Numbers[i] = i * i * i

for key, value in Numbers.items():
    print('Ключ:', key, 'Значение:', value)