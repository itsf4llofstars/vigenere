"""vigenere.py class file"""
from collections import deque


class Vigenere:
    """Vigenere class"""
    def __init__(self,key: str) -> None:
        letters = [
            'A', 'B', 'C', 'D', 'E,' 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        rotor = deque([
            'A', 'B', 'C', 'D', 'E,' 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])
        self.key = list(key)
        self.message = ''
        self.encoded_message = ''


def main():
    """main function"""


if __name__ == "__main__":
    main()
