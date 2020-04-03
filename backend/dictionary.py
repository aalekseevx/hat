import random
from singleton import singleton


class DictionaryInstance:
    def __init__(self, filename) -> 'initialization from file':
        self.word_list = []
        self.dictionary = []
        with open(f"dictionaries_data/{filename}", encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                a = line.split()
                self.word_list.append(a[0])
                self.dictionary = self.dictionary + [a]
        self.dictionary = dict(self.dictionary)

    def get_dict_for_game(self, numb, complexity, variation) -> dict:
        dict_copy = self.dictionary.copy()
        inf = max(1, complexity - variation)
        sup = min(100, complexity + variation)
        good_dict = {}
        iter_dict = {}
        while len(good_dict) < numb:
            for key in list(iter_dict.keys()):
                del dict_copy[key]
            iter_dict = {}
            for key, value in dict_copy.items():
                if int(value) >= inf:
                    if int(value) <= sup:
                        iter_dict.update({key: value})
            good_dict.update(iter_dict)
            inf = max(inf - 1, 1)
            sup = min(100, sup + 1)
        ret_dict = {}
        for i in range(numb):
            key = random.choice(list(good_dict.keys()))
            val = good_dict.pop(key)
            ret_dict.update({key: val})
        return ret_dict

    def add_word(self, word, complexity):
        complexity = min(complexity, 100)
        complexity = max(1, complexity)
        self.dictionary.update({word: complexity})

    def del_word(self, word):
        if word in self.dictionary:
            self.dictionary.pop(word)

    def __len__(self) -> int:
        return len(self.dictionary)

    def pop_random_word(self) -> 'delete 1 random word':
        word = random.choice(self.word_list)
        self.del_word(word)
        return word


@singleton(DictionaryInstance)
class Dictionary:
    pass