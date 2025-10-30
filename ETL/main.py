from extract import extract_data, save_raw_data
from process import transform_data, save_clean_data
from save import load_to_postgres
from validation import validate_output_data
import click

"""
Задаем аргументы: 
input - по умолчанию googlr drive, но можно изменить
limit - количество строк для обработки и сохранения в БД
output_db - название талбицы в БД, по умолчанию 'makoveev'
"""


@click.command()
@click.option(
    "--input",
    default="https://drive.google.com/uc?id=15_7a8dD35xB1WMn5Vl6Z3yAfTIDX3jDh",
    help="Input file path or URL (default: Google Drive)",
)
@click.option("--limit", default=100, help="Limit number of rows to process")
@click.option("--output-db", default="makoveev", help="Output database table name")


# ETL-функция
def main(input, output_db, limit):
    print("ЗАПУСК ETL ПРОЦЕССА")
    print("=" * 50)

    # 1. Извлечение данных
    raw_data = extract_data(input)
    save_raw_data(raw_data)

    # 2. Обработка данных
    clean_data = transform_data(raw_data)

    save_clean_data(clean_data)

    # 3. Выгрузка данных
    load_to_postgres(clean_data, limit, output_db)

    # 4. Валидация данных
    validate_output_data()

    print("\nETL ПРОЦЕСС УСПЕШНО ЗАВЕРШЕН!")
    print("=" * 50)


if __name__ == "__main__":
    main()
