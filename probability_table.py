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
for index, word in enumerate(words):
    if index < len(words) - 1:
        if word in probability_table:
            probability_table[word].append(words[index + 1])
        else:
            probability_table[word] = [words[index + 1]]
