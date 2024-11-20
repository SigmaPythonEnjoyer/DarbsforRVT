from collections import Counter

word_sentiments = {
    "pozitīvi": ["lielisks", "apmierināts", "pozitīvs", "laimīgs", "izcils"],
    "negatīvi": ["vīlies", "neapmierināts", "slikts", "neatbilst"],
}

def noskani_analize(teikums):
    vardi = teikums.lower().split()
    sentiment_counts = Counter()

    for vards in vardi:
        for sentiment, word_list in word_sentiments.items():
            if vards in word_list:
                sentiment_counts[sentiment] += 1

    if sentiment_counts["pozitīvi"] > sentiment_counts["negatīvi"]:
        return "Pozitīvs"
    elif sentiment_counts["negatīvi"] > sentiment_counts["pozitīvi"]:
        return "Negatīvs"
    else:
        return "Neitrāls"

teikumi = [
    "Šis produkts ir lielisks , esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

rezultati = [noskani_analize(teikums) for teikums in teikumi]
print(rezultati)
