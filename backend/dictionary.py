import random
import string


class Dictionary:
    def __init__(self, filename):
        self.dictionary = []
        with open(filename) as f:
            while True:
                line = f.readline()
                if not line: break
                a = line.split()
                b = [a]
                self.dictionary = self.dictionary + b
        self.dictionary = dict(self.dictionary)

    def GetDictForGame(self, numb, complex, variation):
        inf = max(1, complex - variation)
        sup = min(100, complex + variation)
        good_dict = {}
        for ke, value in self.dictionary.items():
            if int(value) >= inf:
                if int(value) <= sup:
                    good_dict.update({ke: value})
                else:
                    break
        ret_dict = {}
        for i in range(numb):
            key = random.choice(list(good_dict.keys()))
            val = good_dict.pop(key)
            ret_dict.update({key: val})
        return ret_dict
