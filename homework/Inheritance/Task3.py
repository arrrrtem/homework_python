"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""

class SpaceObject:
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness

    def shine(self):
        print(f"The star is shining with brightness {self.brightness}.")


class Planet(SpaceObject):
    def __init__(self, size, population, growth_rate):
        super().__init__(size)
        self.population = population
        self.growth_rate = growth_rate

    def calculate_population(self, years):
        for year in range(1, years + 1):
            self.population += int(self.population * (self.growth_rate / 100))
        print(f"After {years} years, the population is {self.population}.")


# Создаем экземпляр класса Star
sun = Star(size="large", brightness="high")

# Вызываем метод светить
sun.shine()

# Создаем экземпляр класса Planet
earth = Planet(size="medium", population=7_900_000_000, growth_rate=1.2)

# Вызываем метод расчета населения
earth.calculate_population(10)
