# Engineering-Data-Management
## Введение 
Датасет содержит информацию о стиях пива, приготовленного домашними пивоварам и основные характеристики получившегося продукта. Работа направлена на обработку и анализ имеющихся данных. 

## Ссылки
[Датасет](https://disk.yandex.ru/d/zoS7hgaKhiFQzA)
[Источник](https://www.kaggle.com/datasets/jtrofe/beer-recipes)

Результат работы скрипта Data_loader.py приведен ниже

<img width="487" height="192" alt="Screenshot_12" src="https://github.com/user-attachments/assets/824dc842-ae9d-4c3b-b4f6-fac41d6b0115" />

## Начало работы

1) Установить miniconda
  
   [На сайте](https://www.anaconda.com/docs/getting-started/miniconda/install)

4) Создание и активация виртуального окружения conda:

```
conda create -n your_name python=3.13 
conda activate your_name
```

3) Установить poetry:

```
pip install poetry
```
4) Создать папку проекта и перейти в папку:
```
poetry new projet_name
cd project_name
```
5) Загрузить нужные библиотеки:
```
poetry add pandas matplotlib jupyterlab wget
```
Полный список используемых библиотек приведен в файле pyproject.toml

6) Запустить скрипт Data_loader.py:
```
poetry run python data_loader.py
```
## Структура проекта
```
Engineering-Data-Management
└──EDA notebook
    ├──EDA.ipynb # Ноутбук с кодом EDA
    ├──Readme.md # Описание EDA
├──Data_loader.py # Скрипт загрузки датасета
├──README.md # Описание проекта
├──environment.yml # Зависимости виртулаьного окружения conda
├──pyproject.toml # конфигурация проекта
└──write_to_db.py # скрипт записи датасета в базу данных
```

