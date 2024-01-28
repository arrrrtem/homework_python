"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом кооржинат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Unsupported operand type for +: Vector3D and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("Unsupported operand type for -: Vector3D and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            # Скалярное произведение векторов
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            # Умножение вектора на скаляр
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise ValueError("Unsupported operand type for *: Vector3D and {type(other)}")

# Пример использования класса Vector3D
if __name__ == "__main__":
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)

    print("Vector 1:", v1)
    print("Vector 2:", v2)

    # Сложение векторов
    sum_result = v1 + v2
    print("Sum:", sum_result)

    # Вычитание векторов
    sub_result = v1 - v2
    print("Subtraction:", sub_result)

    # Скалярное произведение
    scalar_product = v1 * v2
    print("Scalar Product:", scalar_product)

    # Умножение вектора на скаляр
    scalar_multiply = v1 * 2
    print("Scalar Multiply:", scalar_multiply)
