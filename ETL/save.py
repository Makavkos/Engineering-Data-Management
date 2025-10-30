import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import os


def load_to_postgres(clean_data, limit=100, output_db="makoveev"):
    print("\n" + "=" * 50)
    print("ЭТАП 3: ЗАГРУЗКА В POSTGRESQL")
    print("=" * 50)

    # Создаем подключение к PostgreSQL
    def create_postgres_engine():
        sqlite_conn = sqlite3.connect("creds.db")
        cursor = sqlite_conn.cursor()
        cursor.execute("SELECT * FROM access")
        creds = cursor.fetchone()
        sqlite_conn.close()

        connection_string = (
            f"postgresql://{creds[2]}:{creds[3]}@{creds[0]}:{creds[1]}/homeworks"
        )
        engine = create_engine(connection_string)
        return engine

    engine = create_postgres_engine()
    print("Подключение к БД установлено")

    # Используем переданный датасет
    df = clean_data.head(limit)  # Обрезка до 100 строк
    print(f"Данные обрезаны до {limit} строк")

    # Записываем в БД
    table_name = output_db
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Данные записаны в таблицу: {table_name}")

    engine.dispose()

    # Сохраняем датафрейм в Parquet
    file_path = "data/processed/final_data.parquet"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_parquet(file_path, index=False)
    print(f"Финальные данные сохранены: {file_path}")


if __name__ == "__main__":
    print("Загрузка датасета")
    print("=" * 50)
    data = pd.read_parquet("data/processed/clean_data.parquet")

    load_to_postgres(data)
