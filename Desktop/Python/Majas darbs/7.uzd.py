import gensim.downloader as api

model = api.load("word2Vec-google-news-300")

words = ["māja", "dzīvoklis", "jūra"]

for word in words:
    vector = model[word]
    print(f"Word: {word}, Vector: {vector[:5]}...")
