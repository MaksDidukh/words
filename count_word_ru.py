# Открываем файл для чтения
with open('data_ru.txt', 'r') as file:
    # Создаем словарь для подсчета количества слов
    word_count = {}

    # Читаем файл построчно
    for line in file:
        # Разделяем строку на слова
        words = line.split()

        # Обходим каждое слово и увеличиваем счетчик в словаре
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# Открываем файл для записи
with open('word_count.txt', 'w') as file:
    # Сортируем словарь по количеству повторений слов в порядке убывания
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Записываем наиболее часто встречающиеся слова и их количество повторений в файл
    for word, count in sorted_words:
        file.write(f'{word}: {count}\n')
