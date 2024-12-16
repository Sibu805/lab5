#Код
# Откройте и прочитайте файл
# Найдите все слова, оканчивающиеся на "е"
# Найдите все числа в круглых скобках
# Распечатайте результаты
 
import re

file1_data = open('task1-en.txt', 'r').read()

words_suffx_e = re.findall(r'\b\w*e\b', file1_data)
numbers_in_parentheses = re.findall(r'\((\d+)\)', file1_data)


print("Слова, заканчивающиеся на 'e':", words_suffx_e)
print("Цифры в круглых скобках :", numbers_in_parentheses)
