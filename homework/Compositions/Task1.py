"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""


class Profile:
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.passport = passport

    def print_info(self):
        print(f"Name: {self.name}, Last Name: {self.last_name}, Age: {self.age}, Passport: {self.passport}")


class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role:
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked


class BankAccount:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance


class Order:
    def __init__(self, item, date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price


class User:
    def __init__(self, profile):
        self.profile = profile
        self.address = None
        self.role = None
        self.bank_account = None
        self.orders = []

    def set_address(self, city, street, zipcode):
        self.address = Address(city, street, zipcode)

    def set_role(self, role, hours_worked):
        self.role = Role(role, hours_worked)

    def link_bank_account(self, card_number, balance):
        self.bank_account = BankAccount(card_number, balance)

    def add_order(self, item, date, delivery, price):
        order = Order(item, date, delivery, price)
        self.orders.append(order)
