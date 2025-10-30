import pandas as pd
import sqlite3
from sqlalchemy import create_engine, inspect


def validate_output_data():
    print("\n" + "=" * 50)
    print("ЭТАП 4: ВАЛИДАЦИЯ ДАННЫХ")
    print("=" * 50)

    # 1. Валидация сырых данных
    print("\n1. СЫРЫЕ ДАННЫЕ")
    try:
        raw_data = pd.read_csv("data/raw/raw_data.csv")
        print(f"Загружено: {len(raw_data)} строк, {len(raw_data.columns)} столбцов")
        print(f"  Столбцы: {list(raw_data.columns)}")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")

    # 2. Валидация обработанных данных
    print("\n2. ОБРАБОТАННЫЕ ДАННЫЕ")
    try:
        clean_data = pd.read_parquet("data/processed/clean_data.parquet")
        print(f"Загружено: {len(clean_data)} строк, {len(clean_data.columns)} столбцов")

        # Проверка пропусков
        missing_values = clean_data.isnull().sum().sum()
        print(f"  Пропуски: {missing_values}")

        # Проверка дубликатов
        duplicates = clean_data.duplicated().sum()
        print(f"  Дубликаты: {duplicates}")

    except Exception as e:
        print(f"Ошибка загрузки: {e}")

    # 3. Валидация финальных данных
    print("\n3. ФИНАЛЬНЫЕ ДАННЫЕ")
    try:
        final_data = pd.read_parquet("data/processed/final_data.parquet")
        print(f"Загружено: {len(final_data)} строк, {len(final_data.columns)} столбцов")

        # Проверка ограничения строк
        if len(final_data) <= 100:
            print(f"Ограничение строк: <= 100")
        else:
            print(f"Превышено ограничение строк")

    except Exception as e:
        print(f"Ошибка загрузки: {e}")

    # 4. Валидация данных в PostgreSQL
    print("\n4. ДАННЫЕ В POSTGRESQL")
    try:
        # Подключение к PostgreSQL
        sqlite_conn = sqlite3.connect("creds.db")
        cursor = sqlite_conn.cursor()
        cursor.execute("SELECT * FROM access")
        creds = cursor.fetchone()
        sqlite_conn.close()

        connection_string = (
            f"postgresql://{creds[2]}:{creds[3]}@{creds[0]}:{creds[1]}/homeworks"
        )
        engine = create_engine(connection_string)

        # Проверка существования таблицы
        inspector = inspect(engine)
        table_name = "makoveev"
        tables = inspector.get_table_names()

        if table_name in tables:
            count_result = pd.read_sql(
                f"SELECT COUNT(*) as count FROM {table_name}", engine
            )
            row_count = count_result["count"].iloc[0]
            print(f"Таблица '{table_name}' найдена")
            print(f"  Количество строк: {row_count}")
        else:
            print(f"Таблица '{table_name}' не найдена")

        engine.dispose()

    except Exception as e:
        print(f"Ошибка подключения: {e}")

    # 5. Проверка целостности данных
    print("\n5. ЦЕЛОСТНОСТЬ ДАННЫХ")
    try:
        raw_cols = len(raw_data.columns)
        clean_cols = len(clean_data.columns)
        final_cols = len(final_data.columns)

        print(f"  Столбцов в сырых данных: {raw_cols}")
        print(f"  Столбцов в обработанных: {clean_cols}")
        print(f"  Столбцов в финальных: {final_cols}")

        if raw_cols >= clean_cols and clean_cols == final_cols:
            print("Целостность столбцов сохранена")
        else:
            print("Нарушена целостность столбцов")

    except Exception as e:
        print(f"Ошибка проверки: {e}")

    print("\n" + "=" * 50)
    print("ВАЛИДАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)


if __name__ == "__main__":
    validate_output_data()
