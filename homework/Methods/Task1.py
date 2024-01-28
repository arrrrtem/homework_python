"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

    @classmethod
    def create_person_by_birth_year(cls, name, birth_year):
        # Генерация нового объекта с установкой возраста
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        # Проверка на совершеннолетие
        return age >= 18

# Пример использования класса Person
if __name__ == "__main__":
    person1 = Person("Иван", 25)
    person1.display_info()

    # Создание объекта с установкой возраста через метод класса
    person2 = Person.create_person_by_birth_year("Мария", 1990)
    person2.display_info()

    # Проверка на совершеннолетие через статический метод
    age_to_check = 20
    if Person.is_adult(age_to_check):
        print("Человек совершеннолетний.")
    else:
        print("Человек несовершеннолетний.")
