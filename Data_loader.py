import pandas as pd

FILE_ID = "15_7a8dD35xB1WMn5Vl6Z3yAfTIDX3jDh"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url, encoding= 'cp1251')    # читаем файл, устанавливем определенный тип декодирования 

print (raw_data.head(10))         # выводим на экран первые 10 строк для проверки

print (raw_data.dtypes) # Определение типов данных 

print("Пропуски по столбцам:")
print(raw_data.isnull().sum()) #выявление пропусков

raw_data ['SugarScale']=raw_data['SugarScale'].astype('category') # Приведение колонки SugarScale к типу данных category
print(raw_data.SugarScale)

raw_data ['BrewMethod']=raw_data['BrewMethod'].astype('category') # Приведение колонки BrewMethod к типу данных category
print(raw_data.BrewMethod)

raw_data ['Style']=raw_data['Style'].astype('category') # Приведение колонки Style к типу данных category
print(raw_data.Style)

raw_data ['PrimingMethod']=raw_data['PrimingMethod'].astype('category') # Приведение колонки PrimingMethod к типу данных category
print(raw_data.PrimingMethod) 

print (raw_data.dtypes) # Проверка внесенных изменений 
#Name, URL, PrimingAmount не изменял, так как значения в них слишком хаотичные, включающие буквы и цифры, так что ни под категории, ни под что-то еще они не подходят (но возможно я заблуждаюсь)
