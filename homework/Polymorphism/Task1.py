"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Duck:
    def quack(self):
        print("Кря-кря")

    def wear_clothes(self):
        print("Утка носит одежду")

class Human:
    def quack(self):
        print("Человек имитирует кряканье")

    def wear_clothes(self):
        print("Человек носит одежду")

duck1 = Duck()
human1 = Human()

items = [duck1, human1]

for item in items:
    item.quack()
    item.wear_clothes()
