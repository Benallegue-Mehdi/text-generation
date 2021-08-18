text = ''

with open('training_text.txt', 'r') as file:
    for line in file:
        text += line.replace('\n', ' ').replace(' !', '!').replace(' ?', '?').replace(' :', ':').replace(' ;', ';').replace('« ', '').replace(' »', '')

END = object()
words = [END]
words += text.split()

end_punctuation = ['.', '!', '?']
for pos, word in enumerate(words):
    if word != END:
        if word[-1] in end_punctuation:
            words.insert(pos + 1, END)

probability_table = {}
for word in set(words):
    next_words, next_words_indices = [], []
    for index, string in enumerate(words):
        if string == word:
            if index == len(words) - 1:
                pass
            else:
                next_words_indices.append(index + 1)
    
    for index in next_words_indices:
        next_words.append(words[index])
    probability_table[word] = next_words
