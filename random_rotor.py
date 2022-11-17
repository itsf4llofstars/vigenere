"""Creates a 26 letter list with the
letters randomly placed
"""
import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

random_letters_list = []


def create_list():
    """DOC"""
    while len(random_letters_list) != len(letters):
        letter = random.choice(letters)
        if not letter in random_letters_list:
            random_letters_list.append(letter)


def main():


if __name__ == "__main__":
    main()
