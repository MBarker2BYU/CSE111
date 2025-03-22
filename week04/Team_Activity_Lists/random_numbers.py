
from os import system, name
import random


numbers = [13.7, 62.9, 321.4]

suits = ['Spades', 'Dimonds', 'Clubs', 'Hearts']
random_words = []
words = []

def clear_screen():
        system("cls" if name == "nt" else "clear")

def append_random_numbers(numbers_list, quantity=1):
    
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(0,1775),1))

def append_random_words(words_list, quantity=1):
    for _ in range(quantity):
        words_list.append(random_words[random.randint(0,51)])

def create_deck_of_cards(random_word_list):

    for suit in suits:
        for index in range(1, 14):
             
            if index == 1:
                random_word_list.append(F"Ace of {suit}")   
            elif index == 11:
                random_word_list.append(F"Jack of {suit}")
            elif index == 12:
                random_word_list.append(F"Queen of {suit}")
            elif index == 13:
                random_word_list.append(F"King of {suit}")
            else:
                random_word_list.append(F"{index} of {suit}")


def main():
    
    create_deck_of_cards(random_words)

    clear_screen()
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(words, 3)
    print(words)

    append_random_words(words, 1)
    print(words)

    append_random_words(words, 3)
    print(words)

if __name__ == "__main__":
    main()