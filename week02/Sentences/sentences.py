# Author: Matthew D. Barker
# Date: Mar 05, 2025
# Description: Milestone Sentences Assignment
 
from enum import Enum
from random import choice
from os import system, name

class WordType(Enum):
    Determiner = 0
    Noun = 1
    Verb = 2

class Tense(Enum):
    Past = 0
    Present = 1
    Future = 2

class Quantity(Enum):
    Singular = 0
    Plural  = 1


def clear_screen():

    system("cls" if name == "nt" else "clear")

def spacing(lines = 1):

        for _ in range(lines):
            print("")


words = {}

words[(WordType.Determiner, Quantity.Singular)] = ["a", "one", "the"]
words[(WordType.Determiner, Quantity.Plural )] = ["some", "many", "the"]

words[(WordType.Noun, Quantity.Singular)] = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
words[(WordType.Noun, Quantity.Plural )] = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

words[(WordType.Verb, Tense.Past)] = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
words[(WordType.Verb, Tense.Present, Quantity.Singular)] = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
words[(WordType.Verb, Tense.Present, Quantity.Plural )] = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
words[(WordType.Verb, Tense.Future)] = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    #   if quantity == 1:
    #       words = ["a", "one", "the"]
    #   else:
    #       words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = choice(words[(WordType.Determiner, quantity)])
    return word
    

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
        """
    word = choice(words[(WordType.Noun, quantity)])
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    key = (WordType.Verb, tense, quantity)if tense == Tense.Present else (WordType.Verb, tense)

    word = choice(words[key])
    return word


def make_sentence(quantity, tense):
  
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    return F"{determiner.capitalize()} {noun} {verb}."
    
def main():
    
    clear_screen()

    print(make_sentence(Quantity.Singular, Tense.Past))
    print(make_sentence(Quantity.Singular, Tense.Present))
    print(make_sentence(Quantity.Singular, Tense.Future))
    print(make_sentence(Quantity.Plural , Tense.Past))
    print(make_sentence(Quantity.Plural , Tense.Present))
    print(make_sentence(Quantity.Plural , Tense.Future))

    spacing(2)

    print("Have a blessed Day!")

    spacing(2)


main()