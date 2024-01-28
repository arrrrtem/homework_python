"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests

def save_cat_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def main():
    # Ссылки на случайные котики
    random_cat_urls = [
        'https://cataas.com/cat?sort=random&format=json',
        'https://cataas.com/cat?sort=random&format=json',
    ]

    # Ссылки на оригинальные картинки
    original_cat_urls = [
        'https://cataas.com/cat/5c92e7272d72a200197b23f5',
        'https://cataas.com/cat/5d6f330c1555e903f915d7f5',
    ]

    # Ссылки на пиксельные картинки
    pixel_cat_urls = [
        'https://cataas.com/cat/smol/5c92e7272d72a200197b23f5',
        'https://cataas.com/cat/smol/5d6f330c1555e903f915d7f5',
    ]

    # Сохраняем картинки
    for i, url in enumerate(random_cat_urls + original_cat_urls + pixel_cat_urls):
        filename = f'cat_image_{i+1}.jpg'
        save_cat_image(url, filename)
        print(f'Изображение {i+1} сохранено как {filename}')

if __name__ == "__main__":
    main()
