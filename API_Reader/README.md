# API-reader

Мой API - рецепты коктейлей: 	https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita

Под данную задачу создавалось отдельное переменное окружение

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
poetry add pandas matplotlib jupyterlab wget requests
```
6) Запустить скрипт API_reader:
```
poetry run python API_reader.py
```

Скриншот работы скрипта: 

<img width="990" height="506" alt="image" src="https://github.com/user-attachments/assets/4f2845b5-e830-4266-b432-11658c2f1bb5" />

