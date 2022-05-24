
from random import randint
import linecache

discovered_letter_indexes = []


def get_english_word():
    """
    Returns a random word from words.txt wich contains over 370k english words.
    """
    random_index = randint(1, 370105)
    random_word = linecache.getline('words.txt', random_index)
    return random_word[:-1]


word = get_english_word()
word_length = len(word)


def get_single_letter_input():
    """
    Returns the letter given by the user.

    Gets a single letter as input and checks wether it is a valid input by checking its length.    
    """
    print("Enter your Guess: ")
    letter_input = input()
    if len(letter_input) == 1:
        return letter_input.lower()
    else:
        print("Invalid Input! Please enter a single Letter!")
        return get_single_letter_input()


def check_if_word_contains_letter(letter):
    """
    Returns wether the given letter is in the searched word or not.
    """
    if not letter in word:
        return False
    else:
        return True


def get_letter_placements(letter):
    """
    Returns all positions of letter in word as a list.
    """
    indexes = []
    letter_not_found = False
    lower_search_limmit = 0

    # Loop through the word until the Letter is not found anymore.
    while not letter_not_found:
        index = word.find(letter, lower_search_limmit)
        if index == -1:
            letter_not_found = True
            break

        indexes.append(index)
        lower_search_limmit = index+1

    return indexes


def user_loop():
    """
    A Loop of all actions performed following the input of a single letter.
    """
    letter = get_single_letter_input()
    check_if_word_contains_letter(letter)
    discovered_letter_indexes[:] = discovered_letter_indexes + \
        get_letter_placements(letter)


def get_current_word_state():
    """
    Returns a string representing all letters that have been guessed so far.
    """
    current_word_state = ""
    for index in range(word_length):
        if index in discovered_letter_indexes:
            current_word_state += word[index]
        else:
            current_word_state += "_"

    return current_word_state


def main():
    """
    Main Loop of the whole program that ends when the word is found.
    """
    word_found = False
    while(not word_found):
        user_loop()
        current_word_state = get_current_word_state()
        print(current_word_state)
        if not '_' in current_word_state:
            word_found = True

    print("Word Found!")


main()
