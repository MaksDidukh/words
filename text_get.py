import random

# Функция для загрузки файла с текстом и создания списка слов
def load_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = text.split()
        return words
def remove_duplicates(arr):
    # Создаем пустой список для хранения уникальных слов
    unique_words = []
    # Проходим по массиву и добавляем слова в список уникальных слов
    for word in arr:
        # Если слово еще не встречалось, добавляем его в список уникальных слов
        if word not in unique_words:
            unique_words.append(word)
    # Возвращаем список уникальных слов без повторений
    return unique_words
# Функция для предсказания следующих 8 возможных слов
def predict_next_words(words, input_word):
    input_word = input_word.lower()
    possible_words = []
    for i in range(len(words) - 1):
        if words[i] == input_word:
            possible_words.append(words[i + 1])
    if len(possible_words) < 20:
        words = random.sample(possible_words, len(possible_words))
        return remove_duplicates(words)
    words = random.sample(possible_words, 20)
    return remove_duplicates(words)
