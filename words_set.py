import re

def words_set(text: str) -> set:
    words = set(re.split(r'[!\"#\$%&()\*+,\./:;<=>\?@[\]\^_`{|}~ \n]', text.lower()))
    words.remove('')
    return words
