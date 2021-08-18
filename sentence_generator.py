from first_word_proba import first_word_proba
from pick_word import pick_word
from first_word_proba import first_word_proba
import re

with open("training_text.txt", "r") as file:
    text = file.read()
    text = text.replace("\n", "")

result = ""

previous_word = pick_word(first_word_proba(text))
result += previous_word

while True:
    next_word_prob = {}
    possible_next_words = re.findall(rf"(?<={previous_word})[,]? [^!\"#\$%&()\*+,\./:;<=>\?@[\]\^_`|~ \n]+", text)
    if possible_next_words == []:
        result += "."
        break
    else:
        for word in possible_next_words:
            next_word_prob[word] = possible_next_words.count(word) / len(possible_next_words)
        previous_word = pick_word(next_word_prob)
        result += previous_word

print(result)