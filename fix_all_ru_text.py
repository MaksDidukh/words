import re

ru = r'[^а-яА-Я\s]'     # для русского
en = r'[^a-zA-Z\s]'    # для английского
de = r'[^a-zA-ZäöüÄÖÜß\s]'    # для немецкого
pl = r'[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]'    # для польского
es = r'[^a-zA-ZñÑáéíóúüÁÉÍÓÚÜ\s]'    # для испанского
uk = r'[^а-щА-ЩЬьЮюЯяІіЇїЄєҐґ\s]'   # для украинского


# Запрос от пользователя на выбор языка и текста для обработки
language = input("Введите язык (ru, en, de, pl, es, uk): ")
# Запрашиваем название входного файла
input_file = input("Введите название входного файла (без расширения): ")
if not input_file:
    print("Название входного файла не задано. Файл будет назван 'input.txt'.")
    input_file = 'input'

# Запрашиваем название выходного файла
output_file = input("Введите название выходного файла (без расширения): ")
if not output_file:
    print("Название выходного файла не задано. Файл будет назван 'output.txt'.")
    output_file = 'output'


# Выбор регулярного выражения в зависимости от выбранного языка
if language == "ru":
    regex = ru
elif language == "en":
    regex = en
elif language == "de":
    regex = de
elif language == "pl":
    regex = pl
elif language == "es":
    regex = es
elif language == "uk":
    regex = uk
else:
    print("Ошибка: неверно выбран язык")
    exit()




# Открываем исходный файл и создаем файл для записи результата
with open(f"{input_file}.txt", 'r', encoding='utf-8') as file:
    data = file.read()
    # Используем регулярное выражение для удаления всех символов, кроме слов
    data = re.sub(regex, '', data)
    # Приводим все буквы к нижнему регистру
    data = data.lower()
    # Заменяем множественные пробелы на один пробел
    data = re.sub(r'\s+', ' ', data)

with open(f"{output_file}.txt", 'w', encoding='utf-8') as result_file:
    result_file.write(data)
