#Код
# Откройте и прочитайте входной файл со смешанными данными
# Регулярные выражения для каждого типа данных
# Извлеките данные с помощью регулярных выражений
# Убедитесь, что у нас есть совпадающие номера в каждом поле для создания строк
# Создайте таблицу в правильном порядке
# Запишите таблицу в CSV-файл

import re
import csv

with open('task3.txt', 'r') as file:
    file_data = file.read()

id_pattern = r'\b\d+\b'  
surname_pattern = r'\b[A-Z][a-z]+\b'  
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'  
date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'  
website_pattern = r'\bhttps?://[a-zA-Z0-9.-]+\b'  


ids = re.findall(id_pattern, file_data)
surnames = re.findall(surname_pattern, file_data)
emails = re.findall(email_pattern, file_data)
dates = re.findall(date_pattern, file_data)
websites = re.findall(website_pattern, file_data)

rows = min(len(ids), len(surnames), len(emails), len(dates), len(websites))

table = []
for i in range(rows):
    table.append([ids[i], surnames[i], emails[i], dates[i], websites[i]])

with open('task3_output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ID', 'Last Name', 'Email', 'Registration Date', 'Website'])  
    writer.writerows(table)

print("Task 3:Данные нормализованы и сохранены в  'task3_output.csv'.")
