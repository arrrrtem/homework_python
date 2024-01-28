"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""


import sqlite3

# Создание базы данных и таблиц
def create_tables():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            reader_id INTEGER,
            FOREIGN KEY (reader_id) REFERENCES readers (id)
        )
    ''')
    conn.commit()
    conn.close()

# Добавление читателя
def add_reader(name):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO readers (name) VALUES (?)", (name,))
    reader_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return reader_id

# Добавление книги
def add_book(title, author, reader_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, reader_id) VALUES (?, ?, ?)", (title, author, reader_id))
    conn.commit()
    conn.close()

# Вывод всех книг для заданного читателя
def get_books_for_reader(reader_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE reader_id=?", (reader_id,))
    books = cursor.fetchall()
    conn.close()
    return books

# Пример использования функций
create_tables()

reader_name = input("Введите имя читателя: ")
reader_id = add_reader(reader_name)

add_book("Книга 1", "Автор 1", reader_id)
add_book("Книга 2", "Автор 2", reader_id)

books_for_reader = get_books_for_reader(reader_id)

print(f"\nКниги для читателя {reader_name}:")
for book in books_for_reader:
    print(f"Название: {book[1]}, Автор: {book[2]}")
