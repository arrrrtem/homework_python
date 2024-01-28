"""
Создайте базу данных пользователя состояющую из следующих столбцов: id,username,password(В виде хэша).
Создайте программу которая предлагает пользователю зарегистрироваться или авторизироваться.
При регистрации программа запрашивает логин и пароль и добавляет в базу данных нового пользователя.
При авторизации программа запрашивает логин и пароль и выводит сообщение об успешной/неуспешной авторизации.
"""

import sqlite3
import hashlib

# Создание базы данных и таблицы
def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Регистрация нового пользователя
def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Хеширование пароля
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Проверка наличия пользователя с таким именем
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Пользователь с таким именем уже существует.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        print("Регистрация успешна.")
        conn.commit()

    conn.close()

# Авторизация пользователя
def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Хеширование введенного пароля
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        print("Авторизация успешна.")
    else:
        print("Неверное имя пользователя или пароль.")

    conn.close()

# Пример использования функций
create_table()

while True:
    print("\n1. Регистрация\n2. Авторизация\n3. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        username = input("Введите логин: ")
        password = input("Введите пароль: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Введите логин: ")
        password = input("Введите пароль: ")
        login_user(username, password)
    elif choice == "3":
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
