# Author: Matthew D. Barker
# Date: Mar 05, 2025
# Description: Sentences Assignment
 
from enum import Enum
from random import choice
from os import system, name

class WordType(Enum):
    Determiner = 0
    Noun = 1
    Verb = 2
    Preposition = 2
    Adjective = 3
    Adverb = 4    

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

words[WordType.Preposition] = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below",
                                "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over",
                                "past", "to", "under", "with", "without"]

words[WordType.Adjective] = ["adorable", "average", "beautiful", "brave", "calm", "crazy", "defiant", "delightful", "eager", "excited", "fancy", "foolish", "funny", "gifted",
                                "glorious", "healthy", "helpful", "hilarious", "impossible", "inexpensive", "jealous", "joyous", "kind", "lazy", "obedient", "obnoxious", "outrageous", 
                                "outstanding", "perfect", "plain", "poor", "powerful", "puzzled", "rich", "scary", "shy", "smiling", "stormy", "strange", "stupid", "successful", 
                                "super", "tasty", "ugly", "vast", "victorious", "wicked", "worried"]

words[WordType.Adverb] = ["now", "then", "so", "slowly", "incidentally", "immediately", "sadly", "frequently", "commonly", "sweetly", "badly", "dearly", "silently", "willingly", "hardly"]


# Get a random article
def get_determiner(quantity):
    
    return choice(words[(WordType.Determiner, quantity)])
        
#Get a random Noun
def get_noun(quantity):
    
    return choice(words[(WordType.Noun, quantity)])

#get a random verb    
def get_verb(quantity, tense):
    
    key = (WordType.Verb, tense, quantity)if tense == Tense.Present else (WordType.Verb, tense)

    return choice(words[key])
    
# Get a random preposition
def get_preposition():
    
    return choice(words[WordType.Preposition])

# Get a random preposition phrase
def get_prepositional_phrase(quantity):
   
    return F"{get_preposition()} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}"

# Get a random adjective
def get_adjective():
    
    return choice(words[WordType.Adjective])

# Get a random verb
def get_adverb():

    return choice(words[WordType.Adverb])

#Create a sentence that follows the provided format
def make_sentence(quantity, tense):
       
    return (F"{get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} "
            F"{get_adverb()} {get_verb(quantity, tense)} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)}.")

#Produce the six required sentences (The often don't make sense)
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