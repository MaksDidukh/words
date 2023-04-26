from libretranslatepy import LibreTranslateAPI
import time

# Создание экземпляра класса LibreTranslateAPI
translator = LibreTranslateAPI()

# Функция для перевода текста
def translate_text(text):
    result = translator.translate(text, target="ru")
    return result.text

# Открытие исходного файла и создание файла для записи переводов
with open("data.txt", "r", encoding="utf-8") as file:
    with open("output.txt", "w", encoding="utf-8") as output_file:
        # Чтение содержимого файла построчно
        for line in file:
            # Разделение строки на слова
            words = line.split()
            for word in words:
                # Перевод каждого слова
                translated_word = translate_text(word)
                print(f"{word}: {translated_word}\n")
                # Запись слова и его перевода в отдельный файл
                output_file.write(f"{word}: {translated_word}\n")
                # Задержка в 500 миллисекунд
                time.sleep(0.5)
