"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

class BankAccount:
    def __init__(self, name, balance, pasport):
        self._name = name
        self.__balance = balance
        self.__pasport = pasport
        self.__password = None

    def get_balance(self):
        return self.__balance

    def get_pasport(self):
        return self.__pasport

    def change_pasport(self, new_pasport, password):
        if password == self.__password:
            self.__pasport = new_pasport
            print("Номер паспорта успешно изменен.")
        else:
            print("Неверный пароль. Номер паспорта не изменен.")

    def change_balance(self, amount, password):
        if password == self.__password:
            if self.__balance + amount >= 0:
                self.__balance += amount
                print("Баланс успешно изменен.")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Неверный пароль. Баланс не изменен.")

    def delete_pasport_data(self, password):
        if password == self.__password:
            self.__pasport = None
            print("Паспортные данные успешно удалены.")
        else:
            print("Неверный пароль. Паспортные данные не удалены.")

    def set_password(self, password):
        self.__password = password
        print("Пароль успешно установлен.")


# Пример использования:
account = BankAccount(name="John Doe", balance=1000, pasport="1234567890")
account.set_password("secure_password")

print("Баланс:", account.get_balance())
print("Паспорт:", account.get_pasport())

account.change_balance(amount=-500, password="secure_password")
account.change_pasport(new_pasport="0987654321", password="secure_password")

account.delete_pasport_data(password="wrong_password")  # Неверный пароль, не удалит данные

account.delete_pasport_data(password="secure_password")  # Успешное удаление паспортных данных
print("Новый паспорт:", account.get_pasport())
