import re

text1 = """Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."""
text2 = """Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."""

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return set(text.split())

words1 = preprocess(text1)
words2 = preprocess(text2)

common_words = words1 & words2
similarity = len(common_words) / len(words1 | words2) * 100

print(f'Kopīgie vārdi: {common_words}')
print(f'Sakritības līmenis: {similarity:.2f}%')
