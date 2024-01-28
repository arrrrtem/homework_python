"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""

import sqlite3

# Создание базы данных и таблиц
def create_tables():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            experience INTEGER,
            position_id INTEGER,
            FOREIGN KEY (position_id) REFERENCES positions (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Добавление работника
def add_employee(name, experience, position_id):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, experience, position_id) VALUES (?, ?, ?)", (name, experience, position_id))
    conn.commit()
    conn.close()

# Добавление должности
def add_position(title):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO positions (title) VALUES (?)", (title,))
    position_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return position_id

# Вывод всех должностей для заданного работника
def get_positions_for_employee(employee_id):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("SELECT positions.title FROM employees JOIN positions ON employees.position_id = positions.id WHERE employees.id=?", (employee_id,))
    positions = cursor.fetchall()
    conn.close()
    return positions

# Вывод всех работников для заданной должности
def get_employees_for_position(position_id):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE position_id=?", (position_id,))
    employees = cursor.fetchall()
    conn.close()
    return employees

# Вывод всех работников для заданной должности со стажем больше 5
def get_experienced_employees_for_position(position_id):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE position_id=? AND experience > 5", (position_id,))
    employees = cursor.fetchall()
    conn.close()
    return employees

# Пример использования функций
create_tables()

position_id = add_position("Developer")
add_employee("John", 6, position_id)
add_employee("Alice", 4, position_id)

employee_id = 1  # Идентификатор работника (полученный при добавлении)

positions_for_employee = get_positions_for_employee(employee_id)
print(f"\nДолжности для работника (ID {employee_id}):")
for position in positions_for_employee:
    print(f"Должность: {position[0]}")

employees_for_position = get_employees_for_position(position_id)
print(f"\nРаботники для должности (ID {position_id}):")
for employee in employees_for_position:
    print(f"Имя: {employee[1]}, Стаж: {employee[2]}")

experienced_employees_for_position = get_experienced_employees_for_position(position_id)
print(f"\nОпытные работники для должности (ID {position_id}):")
for employee in experienced_employees_for_position:
    print(f"Имя: {employee[1]}, Стаж: {employee[2]}")
