"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__rank = None

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank

    def del_rank(self):
        self.__rank = None

    def victory(self):
        print(f"{self.name} победил в битве!")
        self.set_rank("Победитель арены")

    def defeat(self):
        print(f"{self.name} проиграл в битве.")
        self.del_rank()


# Пример использования:
hero1 = Hero(name="Hero1", health=100)
hero2 = Hero(name="Hero2", health=100)

hero1.victory()  # Устанавливаем звание "Победитель арены" для hero1
print("Звание Hero1:", hero1.get_rank())

hero2.defeat()  # Удаляем звание для hero2
print("Звание Hero2:", hero2.get_rank())
