import random

def pick_word(prob_dict: dict) -> str:
    return random.choices(list(prob_dict.keys()), weights=prob_dict.values(), k=1)[0]
