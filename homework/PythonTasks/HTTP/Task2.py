"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""

import requests

def get_random_user():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    return data['results'][0]

def format_quote(user_data):
    name = f"{user_data['name']['first']} {user_data['name']['last']}"
    country = user_data['location']['country']
    phone = user_data['phone']
    return f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}"

def main():
    random_user = get_random_user()
    quote = format_quote(random_user)
    print(quote)

if __name__ == "__main__":
    main()
