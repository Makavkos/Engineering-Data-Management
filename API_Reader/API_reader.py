import requests
import pandas as pd


url = "https://www.thecocktaildb.com/api/json/v1/1/\
    search.php?s=margarita"  #  Url API
response = requests.get(url)  #  Формирование запроса
"""
Если на запрос у нас успешный ответ, 
то формируем список Coctail_list и записываем в него информацию:
"""
if response.status_code == 200:
    data = response.json()
    Coctail_list =[]
    for drink in data['drinks']:
        cocktail_info = {
            'Название': drink['strDrink'],
            'Категория': drink['strCategory'],
            'Стакан': drink['strGlass'],
            'Алкогольный/Безалкогольный': drink['strAlcoholic'],
            'Класс IBA': drink['strIBA'],}
        Coctail_list.append(cocktail_info)
else:
    print("Ошибка:", response.status_code)

# Перевод списка Coctail_list в pandas DataFrame и сохранение в виде csv файла:
data_frame = pd.DataFrame(Coctail_list)
data_frame.to_csv('cocktails.csv', index=False, encoding='utf-8')
print("Данные сохранены в файл 'cocktails.csv'")

print(data_frame)
