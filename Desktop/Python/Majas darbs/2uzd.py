import langid

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

for text in texts:
    lang, confidence = langid.classify(text)
    print(f'Teksts: "{text}" - Valoda: {lang}')
