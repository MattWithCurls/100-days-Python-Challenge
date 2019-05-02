from data import DICTIONARY, LETTER_SCORES

def load_words():
    # """Load dictionary into a list and return list"""
    mainlist = []
    file = open('dictionary.txt','r')
    for line in file:
        mainlist.extend(line.strip().split(','))
    file.close()
    pass

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0
    for letter in word:
        if letter.isalpha():
            total += LETTER_SCORES[letter.upper()]
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""


    pass

if __name__ == "__main__":
    pass 
    # run unittests to validate