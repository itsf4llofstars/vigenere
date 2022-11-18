"""vigenere.py class file"""
import sys
from collections import deque


class Vigenere:
    """Vigenere class"""

    def __init__(self, key: str) -> None:
        self.letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        self.rotor = deque([
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])
        self.key = list(key.upper())
        self.message = ''
        self.encoded_message = ''
        self.letter = ''
        self.encoded_letter = ''
        self.index = -1

    def __repr__(self) -> str:
        """return a string of attributes"""
        return f'{self.key = }\n{self.message = }\n{self.encoded_message = }\n{self.rotor = }'

    def set_key(self):
        """Sets rotor[0] equal to key[0]"""
        while self.rotor[0] != self.key[0]:
            deque.rotate(self.rotor, -1)

    def rotate_key(self):
        """rotates the key list one letter"""
        self.key.append(self.key.pop(0))

    def rotate_rotor(self):
        """rotates the rotor list one letter"""
        deque.rotate(self.rotor, -1)

    def get_letter(self):
        """DOC"""
        a_letter = str(input("Enter a letter to be encoded [qq to quit]: ")).upper()
        if a_letter == 'QQ':
            sys.exit()
        self.letter = a_letter

    def get_letter_index(self):
        """DOC"""
        self.index = self.letters.index(self.letter)

    def get_letter_at_index(self):
        """DOC"""
        self.encoded_letter = self.rotor[self.index]


def main():
    """main function"""
    vig = Vigenere('HQE')
    vig.set_key()
    vig.get_letter()
    vig.get_letter_index()
    vig.get_letter_at_index()
    print(vig.letter)
    print(vig.index)
    print(vig.encoded_letter)



if __name__ == "__main__":
    main()
