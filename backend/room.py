from dictionary import Dictionary
from functools import reduce
from random import shuffle

word_dictionary = Dictionary("dictionary_ru.txt")


class Room:
    def __init__(self, name: str, username: str):
        self.name = name
        self.status = "game_setup"

        self.stats = {
            username: [0, 0]
        }
        self.pool = None
        self.settings = None
        self.members = {
            username: "online"
        }
        self.queue = None
        self.queue_id = 0
        self.fixed_players = None

    def start_game(self, settings: dict):
        self.settings = settings
        self.pool = list(word_dictionary.get_dict_for_game(self.settings['words'], self.settings['difficulty'],
                                                      self.settings['dispersion']).keys())
        self.fixed_players = list(map(lambda x: x[0], filter(lambda x: x[1] == 'online', self.members.items())))

        self.queue = []
        for delta in range(1, len(self.fixed_players)):
            for idx, person in enumerate(self.fixed_players):
                self.queue.append((person, self.fixed_players[(idx + delta) % len(self.fixed_players)]))

        self.status = 'waiting_round'

    def get_broadcast_data(self):
        return self.__dict__

    def make_offline(self, username):
        self.members[username] = "offline"

    def join(self, username):
        self.members[username] = "online"
        if username not in self.stats:
            self.stats[username] = [0, 0]

    def leave(self, username):
        self.members[username] = "offline"

    def start_round(self):
        self.status = "playing"
        shuffle(self.pool)

    def finish_round(self):
        if self.status != 'waiting_round':
            self.queue_id = (self.queue_id + 1) % len(self.queue)
            self.status = 'waiting_round'

    def remove_word(self, result):
        if result == 'correct':
            self.stats[self.queue[self.queue_id][0]][1] += 1
            self.stats[self.queue[self.queue_id][1]][0] += 1
        self.pool = self.pool[1:]
        if not self.pool:
            self.status = 'show_stats'

    def endgame(self):
        self.status = 'game_setup'
        for key in self.stats:
            self.stats[key] = [0, 0]
        self.queue = None
        self.queue_id = 0
        self.fixed_players = None
