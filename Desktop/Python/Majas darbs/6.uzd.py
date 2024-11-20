from transformers import pipeline

# Загружаем модель для суммирования
summarizer = pipeline("summarization")

text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. 
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. 
Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

# Генерируем суммарный текст
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

# Выводим результат
print(summary[0]['summary_text'])
