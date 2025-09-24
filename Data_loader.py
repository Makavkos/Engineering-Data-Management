import pandas as pd

FILE_ID = "15_7a8dD35xB1WMn5Vl6Z3yAfTIDX3jDh"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url, encoding= 'cp1251')    # читаем файл, устанавливем определенный тип декодирования 

print (raw_data.head(10))         # выводим на экран первые 10 строк для проверки