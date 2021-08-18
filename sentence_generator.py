import random
from probability_table import probability_table, END

current_word = random.choice( probability_table[END])
result = current_word

while True:
    current_word = random.choice( probability_table[current_word])
    if current_word != END:
        result += f' {current_word}'
    else:
        break

print(result)