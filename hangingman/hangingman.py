
word = "youtube"
word_length = len(word)
discovered_letter_indexes = []


def get_single_letter_input():
    print("Enter your Guess: ")
    letter_input = input()
    if len(letter_input) == 1:
        return letter_input.lower()
    else:
        print("Invalid Input! Please enter a single Letter!")
        return get_single_letter_input()


def check_if_word_contains_letter(letter):
    if not letter in word:
        return False
    else:
        return True


def get_letter_placements(letter):
    indexes = []
    letter_not_found = False
    lower_search_limmit = 0
    while not letter_not_found:
        index = word.find(letter, lower_search_limmit)
        if index == -1:
            letter_not_found = True
            break

        indexes.append(index)
        lower_search_limmit = index+1

    return indexes


def user_loop():
    letter = get_single_letter_input()
    check_if_word_contains_letter(letter)
    discovered_letter_indexes[:] = discovered_letter_indexes + \
        get_letter_placements(letter)


def get_current_word_state():
    current_word_state = ""
    for index in range(word_length):
        if index in discovered_letter_indexes:
            current_word_state += word[index]
        else:
            current_word_state += "_"

    return current_word_state


def main():
    word_found = False
    while(not word_found):
        user_loop()
        current_word_state = get_current_word_state()
        print(current_word_state)
        if not '_' in current_word_state:
            word_found = True

    print("Word Found!")


main()
