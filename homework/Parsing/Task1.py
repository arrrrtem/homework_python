"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""

import requests
import json
from bs4 import BeautifulSoup

url = "https://music.yandex.ru/chart"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    chart_data = {}

    # Здесь нужно извлечь данные из soup и сохранить их в chart_data

    with open("chart_data.json", "w", encoding="utf-8") as file:
        json.dump(chart_data, file, ensure_ascii=False, indent=4)
else:
    print("Не удалось получить доступ к странице чартов Яндекс.Музыки")