import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# Подключение к SQLite и получение учетных данных
sqlite_conn = sqlite3.connect('creds.db')
cursor = sqlite_conn.cursor()
cursor.execute("SELECT * FROM access")
creds = cursor.fetchone()
sqlite_conn.close()

# Создание подключения к PostgreSQL через sqlalchemy
connection_string = f"postgresql://{creds[2]}:{creds[3]}@{creds[0]}:{creds[1]}/homeworks"
engine = create_engine(connection_string)

# Чтение датасета
df = pd.read_parquet('df_100.parquet')

# Приведение типов к category
print("Типы ДО преобразования:")
print(df[['SugarScale', 'BrewMethod', 'Style']].dtypes)


df['SugarScale'] = df['SugarScale'].astype('category')
df['BrewMethod'] = df['BrewMethod'].astype('category')
df['Style'] = df['Style'].astype('category')


print("\nТипы ПОСЛЕ преобразования:")
print(df[['SugarScale', 'BrewMethod', 'Style']].dtypes)

# Запись в БД
table_name = "makoveev"
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"\nДанные успешно записаны в таблицу {table_name}")


engine.dispose()