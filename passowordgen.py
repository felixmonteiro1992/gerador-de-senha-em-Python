import string
import random

LETTERS = string.ascii_letters
NUMBER = string.digits
PUNCTUANTION = "@%#_-+=.,"

def generate_passoword(letters=8, numbers=4, punctuation=2):
    generated = ""

    for i in range(letters):
        generated += random.choice(LETTERS)
    for i in range(numbers):
        generated += random.choice(NUMBER)
    for i in range(punctuation):
        generated += random.choice(PUNCTUANTION)

    generated = list(generated)
    random.shuffle(generated)
    return "".join(generated)




print  (generate_passoword())


        