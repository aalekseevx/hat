import random
from typing import Dict, List
from patterns.singleton import singleton


class SimpleDictionary:
    def __init__(self, **kwargs) -> None:
        """SimpleDictionary initialization"""
        self.word_list = []
        if 'filename' in kwargs:
            with open(kwargs['filename'], encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    line = line.rstrip()
                    if not line:
                        break
                    self.word_list.append(line)
        else:
            self.word_list = kwargs['dictionary']

    def get_dict_for_game(self, numb: int) -> List[str]:
        """take random words"""
        dict_copy = list(self.word_list)
        return_dict = []
        for i in range(numb):
            if len(dict_copy) == 0:
                break
            word = random.choice(dict_copy)
            dict_copy.remove(word)
            return_dict.append(word)
        return return_dict

    def add_word(self, word: str) -> None:
        """add word"""
        if word not in self.word_list:
            self.word_list.append(word)

    def del_word(self, word: str) -> None:
        """delete word"""
        if word in self.word_list:
            self.word_list.remove(word)

    def __len__(self) -> int:
        """dictionary size"""
        return len(self.word_list)

    def write_dict_in_file(self, filename: str) -> None:
        """write words in file"""
        dict_copy = self.word_list
        with open(f"dictionaries_data/{filename}", 'w', encoding='utf-8') as f:
            while len(dict_copy):
                f.write(dict_copy[0])
                dict_copy = dict_copy[1:]


class DictionaryInstance:
    def __init__(self, filename: str) -> None:
        """generate dictionary from file"""
        self.word_list = []
        self.dictionary = []
        with open(filename, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                a = line.split()
                self.word_list.append(a[0])
                self.dictionary = self.dictionary + [a]
        self.dictionary = dict(self.dictionary)

    def get_dict_for_game(self, numb: int, complexity: int, variation: int) -> Dict[str, int]:
        """take words for game based on parameters"""
        dict_copy = self.dictionary.copy()
        inf = max(1, complexity - variation)
        sup = min(100, complexity + variation)
        good_dict = {}
        iter_dict = {}
        if numb > len(self.word_list):
            numb = len(self.word_list)
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

    def create_simple_dictionary(self, numb: int, complexity: int, variation: int) -> SimpleDictionary:
        dictionary = self.get_dict_for_game(numb, complexity, variation)
        words = list(dictionary.keys())
        simple_dictionary = SimpleDictionary(**{'dictionary': words})
        return simple_dictionary

    def add_word(self, word: str, complexity: int) -> None:
        """add new word"""
        complexity = min(complexity, 100)
        complexity = max(1, complexity)
        if word not in self.word_list:
            self.word_list.append(word)
        self.dictionary.update({word: complexity})

    def del_word(self, word: str) -> None:
        """delete given word"""
        if word in self.dictionary:
            self.dictionary.pop(word)
            self.word_list.remove(word)

    def __len__(self) -> int:
        """dictionary size"""
        return len(self.dictionary)

    def pop_random_word(self) -> str:
        """delete random word"""
        word = random.choice(self.word_list)
        self.del_word(word)
        return word


@singleton(DictionaryInstance)
class Dictionary:
    pass
