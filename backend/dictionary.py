import random
import string


class Dictionary:
    def __init__(self, filename):
        self.dictionary = []
        with open(filename, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line: break
                a = line.split()
                b = [a]
                self.dictionary = self.dictionary + b
        self.dictionary = dict(self.dictionary)

    def GetDictForGame(self, numb, complex, variation):
        dict_copy = self.dictionary.copy()
        inf = max(1, complex - variation)
        sup = min(100, complex + variation)
        good_dict = {}
        iter_dict = {}
        while len(good_dict) < numb:
            for ki in list(iter_dict.keys()):
                del dict_copy[ki]
            iter_dict = {}
            for ke, value in dict_copy.items():
                if int(value) >= inf:
                    if int(value) <= sup:
                        iter_dict.update({ke: value})
                    else:
                        break
            good_dict.update(iter_dict)
            inf = max(inf - 1, 1)
            sup = min(100, sup + 1)
        ret_dict = {}
        for i in range(numb):
            key = random.choice(list(good_dict.keys()))
            val = good_dict.pop(key)
            ret_dict.update({key: val})
        return ret_dict
