"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""

import sqlite3

# Создание базы данных и таблицы
def create_table():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year INTEGER,
            genre TEXT,
            rating REAL
        )
    ''')
    conn.commit()
    conn.close()

# Добавление фильма в базу
def add_movie(title, year, genre, rating):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, year, genre, rating) VALUES (?, ?, ?, ?)", (title, year, genre, rating))
    conn.commit()
    conn.close()

# Получение всех фильмов
def get_all_movies():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return movies

# Получение фильма по определенному году
def get_movies_by_year(year):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE year=?", (year,))
    movies = cursor.fetchall()
    conn.close()
    return movies

# Обновление рейтинга фильма
def update_rating(movie_id, new_rating):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET rating=? WHERE id=?", (new_rating, movie_id))
    conn.commit()
    conn.close()

# Удаление фильма
def delete_movie(movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    conn.commit()
    conn.close()

# Пример использования функций
create_table()

add_movie("Inception", 2010, "Sci-Fi", 8.8)
add_movie("The Shawshank Redemption", 1994, "Drama", 9.3)

print("All Movies:")
print(get_all_movies())

print("\nMovies from 2010:")
print(get_movies_by_year(2010))

update_rating(1, 9.0)
print("\nUpdated Rating:")
print(get_all_movies())

delete_movie(2)
print("\nMovies after deletion:")
print(get_all_movies())
