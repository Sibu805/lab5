#Код
# Откройте и прочитайте HTML-файл
# Найдите все размеры изображения (атрибуты ширины и высоты)
# Объедините размеры в пары
# then Распечатайте результаты
 
import re 

file2_data = open('task2.html', 'r', encoding='utf-8').read()

dimensions = re.findall(r'width=["\'](\d+)["\'].*?height=["\'](\d+)["\']|height=["\'](\d+)["\'].*?width=["\'](\d+)["\']', file2_data)
image_sizes = [(match[0] or match[3], match[1] or match[2]) for match in dimensions]

print("Размеры изображения (Ширина x высота) :", image_sizes)
