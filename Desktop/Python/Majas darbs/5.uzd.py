import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏 👏 👏 http://example.com"

clean_text = re.sub(r'http\S+|@\S+|[^a-zA-ZāčēģīķļņšūžĀČĒĢĪĶĻŅŠŪŽ\s]', '', raw_text).lower().strip()
print(clean_text)

