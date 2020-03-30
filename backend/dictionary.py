import random


class Dictionary:
    def __init__(self, filename):
        self.dictionary = []
        with open(filename) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                a = line.split()
                b = [a]
                self.dictionary = self.dictionary + b
        self.dictionary = dict(self.dictionary)

    def get_dict_for_game(self, numb, complexity, variation):
        inf = max(1, complexity - variation)
        sup = min(100, complexity + variation)
        good_dict = {}
        for key, value in self.dictionary.items():
            if int(value) >= inf:
                if int(value) <= sup:
                    good_dict.update({key: value})
                else:
                    break
        ret_dict = {}
        for i in range(numb):
            key = random.choice(list(good_dict.keys()))
            val = good_dict.pop(key)
            ret_dict.update({key: val})
        return ret_dict
