#Код
# Откройте и прочитайте файл со случайным шумом
# Шаблоны регулярных выражений
# Даты: соответствуют таким форматам, как ГГГГ-ММ-ДД, ДД/ММ/ГГГГ, ДД.ММ.ГГГГ
# Электронные письма: соответствуют стандартным адресам электронной почты
# Веб-сайты: Сопоставьте URL-адреса, начинающиеся с http или https
# Извлеките совпадения
# Ограничьте количество результатов первыми 5 для каждого типа
# затем распечатайте результаты
 
import re

file_data = open('task_add.txt', 'r').read()

date_patterns = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}\.\d{2}\.\d{4}\b'
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
website_pattern = r'\bhttps?://[a-zA-Z0-9.-]+\b'

dates = re.findall(date_patterns, file_data)
emails = re.findall(email_pattern, file_data)
websites = re.findall(website_pattern, file_data)

dates = dates[:5]
emails = emails[:5]
websites = websites[:5]

print("Extracted Dates:", dates)
print("Extracted Emails:", emails)
print("Extracted Websites:", websites)
