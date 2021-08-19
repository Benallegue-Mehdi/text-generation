import random
from probability_table import probability_table, END

table = probability_table('Bible_Crampon_1923_Genèse.txt')
current_word = random.choice(table[END])
result = current_word

while True:
    current_word = random.choice(table[current_word])
    if current_word != END:
        result += f' {current_word}'
    else:
        break

print(result)
