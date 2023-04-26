import re

# Открываем исходный файл и создаем файл для записи результата
with open('data_ru.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    # Используем регулярное выражение для удаления всех символов, кроме русских слов
    data = re.sub(r'[^а-яА-Я\s]', '', data)
    # Приводим все буквы к нижнему регистру
    data = data.lower()
    # Заменяем множественные пробелы на один пробел
    data = re.sub(r'\s+', ' ', data)

with open('out.txt', 'w', encoding='utf-8') as result_file:
    result_file.write(data)
