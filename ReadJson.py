import re
import string
import pymystem3

from stop_words import get_stop_words
import nltk

file = open('C:/Users/admin/Documents/Folder/bold.json', "r", encoding="utf8")

text = file.read()
loweredText = text.lower()
textWithoutDigits = re.sub(r'\d+', '', loweredText)
textWithoutPunctuation = ''.join(ch for ch in textWithoutDigits if ch not in  set(string.punctuation))
textWoSpaces = " ".join(textWithoutPunctuation.split())

stop_words = get_stop_words('ru')  # https://pypi.org/project/stop-words/

stop_words.append("сообщение")
stop_words.append("сообщения")
stop_words.append("тема")
stop_words.append("здравствуйте")


def remove_stopwords(text):
    tokens = text.split()
    tokens = [token for token in tokens if token not in stop_words \
              and token != " " \
              and token.strip() not in set(string.punctuation)]

    text = " ".join(tokens)
    return text

print("\nText\n" + text[0:1000])
print("\nLowered text\n" + loweredText[0:1000])
print("\nTextWithout digits\n" + textWithoutDigits[0:1000])
print("\nText without punctuation\n" + textWithoutPunctuation[0:1000])
print("\nText without spaces\n" + textWoSpaces[0:1000])
print("\nText without stopwords\n" + remove_stopwords(textWoSpaces)[0:1000])


