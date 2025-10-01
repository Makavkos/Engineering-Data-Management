# Engineering-Data-Management
Датасет - https://disk.yandex.ru/d/zoS7hgaKhiFQzA
Набор рецептур домашнего пива 

Результат работы скрипта Data_loader.py приведен ниже

<img width="487" height="192" alt="Screenshot_12" src="https://github.com/user-attachments/assets/824dc842-ae9d-4c3b-b4f6-fac41d6b0115" />

Для работы с проектом:

1) Клонирование репозитория:

```  git clone <URL-репозитория>  ```

2) Создание и активация виртуального окружения conda:

```
conda create -n your_name python=3.13 
conda activate your_name
```

3) Установить poetry, если требуется:

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
6) Запустить скрипт Data_loader.py:
```
poetry run python data_loader.py
```

Внес изменения в Data_loader.py 

Добавил ноутбук data_loader_notebook.ipynb
