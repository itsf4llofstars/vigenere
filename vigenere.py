"""vigenere.py class file"""
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

    def get_letter_index(self, letter):
        """DOC"""

    def get_letter(self, index):
        """DOC"""


def main():
    """main function"""
    vig = Vigenere('HQE')
    vig.set_key()

    print(vig)

    vig.rotate_key()
    vig.rotate_rotor()

    print(vig)


if __name__ == "__main__":
    main()
