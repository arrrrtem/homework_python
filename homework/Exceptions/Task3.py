"""
Пользователь вводит логин. Программа должна проверить все ли символы являются строчными. Если нет, выбросить ошибку.
Если ошибки не произошло писать фразу "Логин добавлен в базу". В не зависимости от того была ли ошибка должно печататься
"Я выучил исключения"
"""

try:
    # Пользователь вводит логин
    login = input("Введите логин: ")

    # Проверка, что все символы логина строчные
    if not login.islower():
        raise ValueError("Логин должен содержать только строчные символы")

    # Если ошибок не возникло
    print("Логин добавлен в базу")

except ValueError as e:
    # Обработка ошибки, если символы логина не строчные
    print(f"Ошибка: {e}")

finally:
    # Вывод фразы независимо от наличия ошибки
    print("Я выучил исключения")
