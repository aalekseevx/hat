import random
import string


class Dictionary:
    def __init__(self):
        pass

    def pop_random_word(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
