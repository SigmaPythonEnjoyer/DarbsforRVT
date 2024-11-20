from collections import Counter
import re

text = """Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."""
words = re.findall(r'\b\w+\b', text.lower())
word_count = Counter(words)
print(word_count)
