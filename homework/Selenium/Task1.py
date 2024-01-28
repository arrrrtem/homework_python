"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def scrape_steam_strategy_games():
    # Путь к вашему веб-драйверу
    driver_path = 'путь_к_chromedriver/chromedriver'  # Укажите свой путь

    # Запуск веб-драйвера
    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Открываем сайт Steam
        driver.get('https://store.steampowered.com/')

        # Находим поле поиска
        search_box = driver.find_element("id", "store_nav_search_term")

        # Вводим запрос "стратегии" в поле поиска
        search_box.send_keys("стратегии")

        # Отправляем запрос
        search_box.send_keys(Keys.RETURN)

        # Ждем, чтобы страница успела загрузиться
        time.sleep(5)

        # Находим все названия игр на странице
        game_titles = driver.find_elements_by_class_name("search_result_row")

        # Выводим названия игр
        for title in game_titles:
            print(title.get_attribute("data-ds-appid"), title.find_element_by_class_name("title").text)

    finally:
        # Закрываем браузер после использования
        driver.quit()


if __name__ == "__main__":
    scrape_steam_strategy_games()
