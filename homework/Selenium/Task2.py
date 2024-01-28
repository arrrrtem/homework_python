"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""

import requests
from bs4 import BeautifulSoup
import json

def scrape_elzhura_schedule(username, password):
    # Адрес страницы Элжуры с расписанием
    url = 'https://eljur.ru/login'

    # Создаем сессию для работы с куками
    session = requests.Session()

    # Отправляем запрос на страницу входа
    login_page = session.get(url)
    soup = BeautifulSoup(login_page.content, 'html.parser')

    # Находим форму входа
    login_form = soup.find('form', {'id': 'loginForm'})

    # Заполняем данные формы
    payload = {
        'login': username,
        'password': password,
    }

    # Отправляем POST-запрос для входа
    session.post(url, data=payload)

    # После входа находим ссылку на страницу с расписанием
    schedule_link = session.find('a', {'id': 'schedule', 'title': 'Расписание'})

    # Загружаем страницу с расписанием
    schedule_page = session.get(schedule_link['href'])
    schedule_soup = BeautifulSoup(schedule_page.content, 'html.parser')

    # Здесь нужно добавить код для извлечения информации о расписании
    # Например, находим таблицу с расписанием и извлекаем нужные данные

    # Ваш код...

    # Пример сохранения расписания в JSON-файл
    schedule_data = {
        'понедельник': {'Математика': '101', 'Физика': '102'},
        'вторник': {'Химия': '201', 'Иностранный язык': '202'},
        # и так далее...
    }

    with open('schedule.json', 'w') as json_file:
        json.dump(schedule_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    username = input("Введите ваш логин на Элжуре: ")
    password = input("Введите ваш пароль на Элжуре: ")
    scrape_elzhura_schedule(username, password)
