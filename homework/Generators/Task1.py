"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""

def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char

# Пример использования генератора
input_str = "Hello123, World!"
for letter in letter_generator(input_str):
    print(letter)
