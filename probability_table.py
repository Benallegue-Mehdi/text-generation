END = object()

def probability_table(path_to_file: str) -> dict:
    text = ''

    with open(path_to_file, 'r') as file:
        for line in file:
            text += line.replace('\n', ' ').replace(' !', '!').replace(' ?', 
            '?').replace(' :', ':').replace(' ;', ';').replace('« ', 
            '').replace(' »', '')

    words = [END]
    words += text.split()

    end_punctuation = ['.', '!', '?']
    for pos, word in enumerate(words):
        if word != END:
            if word[-1] in end_punctuation:
                words.insert(pos + 1, END)

    probability_table = {}
    previous, *words = words
    for word in words:
        try:
            probability_table[previous].append(word)
        except:
            probability_table[previous] = [word]
        previous = word
    return probability_table