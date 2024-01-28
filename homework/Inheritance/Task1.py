"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"Hero {self.name}, Health: {self.health}")

    def attack(self):
        print(f"{self.name} attacks!")

class Magician(Hero):
    def hello(self):
        print("Hello, I am a magician!")

    def attack(self):
        print(f"{self.name} casts a spell!")

# Пример использования
hero1 = Hero("Warrior", 100)
hero2 = Magician("Wizard", 80)

hero1.show_info()
hero1.attack()

hero2.show_info()
hero2.attack()
hero2.hello()
