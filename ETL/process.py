import pandas as pd
import os


def transform_data(raw_data):
    print("\n" + "=" * 50)
    print("ЭТАП 2: ПРЕОБРАЗОВАНИЕ ДАННЫХ")
    print("=" * 50)

    # Приведение колонок к типу category
    print("Приведение типов данных к category...")
    raw_data["SugarScale"] = raw_data["SugarScale"].astype("category")
    raw_data["BrewMethod"] = raw_data["BrewMethod"].astype("category")
    raw_data["Style"] = raw_data["Style"].astype("category")
    raw_data["PrimingMethod"] = raw_data["PrimingMethod"].astype("category")
    print("Типы данных преобразованы")

    # Удаление колонок с долей пропусков более 30%
    print("\nОбработка пропущенных значений...")

    def remove_high_na_columns(df, threshold=30):
        na_percent = df.isnull().mean() * 100
        columns_to_drop = na_percent[na_percent > threshold].index
        df = df.drop(columns=columns_to_drop)
        return df

    raw_data = remove_high_na_columns(raw_data, threshold=30)
    print("Столбцы с >30% пропусков удалены")

    # Проверка пропусков
    missing_total = raw_data.isnull().sum().sum()
    print(f"  Общее количество пропусков: {missing_total}")

    # Проверка дубликатов
    duplicates = raw_data.duplicated().sum()
    print(f"  Количество дубликатов: {duplicates}")

    return raw_data


def save_clean_data(transformed_data):
    print("\n" + "=" * 50)
    print("СОХРАНЕНИЕ ОБРАБОТАННЫХ ДАННЫХ")
    print("=" * 50)

    # Сохраняем датафрейм в Parquet
    file_path = "data/processed/clean_data.parquet"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    transformed_data.to_parquet(file_path, index=False)
    print(f"Обработанные данные сохранены: {file_path}")
    print(
        f"  Размер: {len(transformed_data)} строк, {len(transformed_data.columns)} столбцов"
    )


if __name__ == "__main__":
    # выгрузка датасета
    raw_data = pd.read_csv("data/raw/raw_data.csv")

    # Вызываем функцию и получаем преобразованный датафрейм
    transformed_data = transform_data(raw_data)

    # Сохраняем данные
    save_clean_data(transformed_data)
