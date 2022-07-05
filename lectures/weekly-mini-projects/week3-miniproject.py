import random

list_ = ['Book', 'Pencil', 'Pen', 'Notebook', 'Bag', 'Ruler']
random_word = len(random.choice(list_)) * '*'

def guess_word():
    i = len(random_word) 
    a = input('Please enter a letter: ')
    while i < len(random_word):
        i += a
    if a not in list_:
        print(random_word)
    else: 
        print('You have not guessed the word :(.')

guess_word()