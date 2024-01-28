"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""

class Student:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name

    def add_genius(self):
        self.name += " гений"


class OOPStudent(Student):
    def print_info(self):
        super().add_genius()
        print(f"{self.name}, но его отчислят если он не будет учить ООП")


# Создаем экземпляр первого класса
student1 = Student()
student1.set_name("John")

# Вызываем метод добавления "гения"
student1.add_genius()

# Выводим имя
print(student1.name)

# Создаем экземпляр второго класса
student2 = OOPStudent()
student2.set_name("Alice")

# Вызываем метод, который добавляет "гения" и выводит информацию
student2.print_info()
