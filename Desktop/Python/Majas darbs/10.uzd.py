from translate import Translator

texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translator = Translator(to_lang="en", from_lang="lv")

for text in texts:
    translation = translator.translate(text)
    print(f'Latviski: "{text}" - Angliski: "{translation}"')
