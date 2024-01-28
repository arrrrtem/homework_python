"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""


import requests
import json

def get_character_info(character_id):
    response = requests.get(f'https://rickandmortyapi.com/api/character/{character_id}')
    data = response.json()
    return data

def get_episode_info(episode_url):
    response = requests.get(episode_url)
    data = response.json()
    return data

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    start_id = 1  # Ваш номер в журнале
    end_id = 5  # Умножьте ваш номер на 5
    characters_info = []

    for character_id in range(start_id, end_id + 1):
        character_data = get_character_info(character_id)

        # Получаем дополнительные данные о каждом эпизоде
        episode_info = [get_episode_info(episode_url) for episode_url in character_data['episode']]

        # Собираем нужные данные о персонаже
        character_info = {
            'name': character_data['name'],
            'planet': character_data['origin']['name'],
            'episodes': [{'name': episode['name'], 'episode': episode['episode']} for episode in episode_info],
        }

        characters_info.append(character_info)

    # Сохраняем в JSON файл
    save_to_json(characters_info, 'characters_info.json')

if __name__ == "__main__":
    main()
