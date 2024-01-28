"""
Из набора данных Titanic.csv выведите:
количество пассажиров,
средний возраст пассажира,
среднуюю стоимость билета,
максимальную и минимальную цену билета,
пассажира с максимальной ценой билета,
средний возраст мужчин и женщин по отдельности,
средний процент выживаемости мужчин и женщин,
среднюю стоимость билета в зависимости от класса проживания,
количество билетов по классам проживания,
количество выживших пассажиров
"""

import pandas as pd

# Загрузка данных из файла Titanic.csv
data = pd.read_csv('Titanic.csv')

# Количество пассажиров
passenger_count = len(data)
print("Количество пассажиров:", passenger_count)

# Средний возраст пассажиров
average_age = data['Age'].mean()
print("Средний возраст пассажиров:", average_age)

# Средняя стоимость билета
average_fare = data['Fare'].mean()
print("Средняя стоимость билета:", average_fare)

# Максимальная и минимальная цена билета
max_fare = data['Fare'].max()
min_fare = data['Fare'].min()
print("Максимальная цена билета:", max_fare)
print("Минимальная цена билета:", min_fare)

# Пассажир с максимальной ценой билета
passenger_with_max_fare = data.loc[data['Fare'].idxmax()]
print("Пассажир с максимальной ценой билета:")
print(passenger_with_max_fare)

# Средний возраст мужчин и женщин
average_age_male = data[data['Sex'] == 'male']['Age'].mean()
average_age_female = data[data['Sex'] == 'female']['Age'].mean()
print("Средний возраст мужчин:", average_age_male)
print("Средний возраст женщин:", average_age_female)

# Средний процент выживаемости мужчин и женщин
survival_percentage_male = data[data['Sex'] == 'male']['Survived'].mean() * 100
survival_percentage_female = data[data['Sex'] == 'female']['Survived'].mean() * 100
print("Средний процент выживаемости мужчин:", survival_percentage_male)
print("Средний процент выживаемости женщин:", survival_percentage_female)

# Средняя стоимость билета в зависимости от класса проживания
average_fare_by_class = data.groupby('Pclass')['Fare'].mean()
print("Средняя стоимость билета по классам проживания:")
print(average_fare_by_class)

# Количество билетов по классам проживания
tickets_by_class = data['Pclass'].value_counts()
print("Количество билетов по классам проживания:")
print(tickets_by_class)

# Количество выживших пассажиров
survived_passengers = data['Survived'].sum()
print("Количество выживших пассажиров:", survived_passengers)
