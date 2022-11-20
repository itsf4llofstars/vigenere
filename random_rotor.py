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


def shuffle_list(number: int = 1000):
    """Shuffle list number times"""
    if number > 0:
        for _ in range(number):
            random.shuffle(random_letters_list)


def print_random_list():
    """print random list"""
    [print(letter, end="") for letter in random_letters_list]
    print()


def main():
    """main"""
    create_list()
    shuffle_list(100000)
    print_random_list()


if __name__ == "__main__":
    main()
