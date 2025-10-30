# extract.py
import pandas as pd
import os


def extract_data(input_file):
    print("\n" + "=" * 50)
    print("ЭТАП 1: ИЗВЛЕЧЕНИЕ ДАННЫХ")
    print("=" * 50)

    if input_file.startswith("http"):
        # Если это URL
        raw_data = pd.read_csv(input_file, encoding="cp1251")
    else:
        # Если это локальный файл
        raw_data = pd.read_csv(input_file, encoding="cp1251")

    print("Данные успешно загружены")
    print(f"  Размер: {len(raw_data)} строк, {len(raw_data.columns)} столбцов")
    print(f"  Столбцы: {list(raw_data.columns)}")

    return raw_data


def save_raw_data(raw_data):
    print("\n" + "=" * 50)
    print("СОХРАНЕНИЕ СЫРЫХ ДАННЫХ")
    print("=" * 50)

    # Задаем путь сохранения
    file_path = "data/raw/raw_data.csv"
    # Создаем директории
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Сохраняем датасет
    raw_data.to_csv(file_path, index=False)
    print(f"Сырые данные сохранены: {file_path}")


if __name__ == "__main__":
    data = extract_data(
        "https://drive.google.com/uc?id=15_7a8dD35xB1WMn5Vl6Z3yAfTIDX3jDh"
    )
    save_raw_data(data)
