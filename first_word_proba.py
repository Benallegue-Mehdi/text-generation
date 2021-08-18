import re

def first_word_proba(text: str) -> dict:
    first_words = []
    for sentence in re.split(r'[.!?] ', text):
        first_words.append(sentence.split(' ')[0])

    probabilities = {}
    for word in set(first_words):
        probabilities[word] = first_words.count(word) / len(first_words)
        return probabilities

