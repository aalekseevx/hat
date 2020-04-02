from random import shuffle
from namedlist import namedlist

import config
from statistics import PartyStatistics

PlayingPair = namedlist('PlayingPair', ['explaining_user', 'guessing_user'])


class GameController:
    def __init__(self):
        self.global_statistics = PartyStatistics([], [])
        self.last_statistics = PartyStatistics([], [])

        self.status = "game_setup"
        self.players = None
        self.word_dictionary = None
        self.settings = None
        self.pool = None
        self.queue = []
        self.queue_id = None

    def start_game_(self, players: list, settings: dict):
        self.status = 'waiting_round'
        self.players = players
        self.word_dictionary = config.AVAILABLE_DICT[settings['dict']]
        self.settings = settings
        self.pool = list(self.word_dictionary.get_dict_for_game(self.settings['words'], self.settings['difficulty'],
                                                                self.settings['dispersion']).keys())

        self.queue = []
        for delta in range(1, len(self.players)):
            for idx, person in enumerate(self.players):
                self.queue.append(PlayingPair(explaining_user=person, guessing_user=self.players[
                    (idx + delta) % len(self.players)]))
        self.queue_id = 0
        self.last_statistics = PartyStatistics(players, self.pool)
        self.global_statistics.add_objects(players, self.pool)

    def start_round(self):
        self.status = "playing"
        shuffle(self.pool)

    def finish_round(self):
        if self.status != 'waiting_round':
            self.queue_id = (self.queue_id + 1) % len(self.queue)
            self.status = 'waiting_round'

    def remove_word(self, verdict, screen_time):
        word = self.pool[0]
        self.last_statistics.add_result(self.queue[self.queue_id].explaining_user,
                                        self.queue[self.queue_id].guessing_user, word, verdict, screen_time)
        self.global_statistics.add_result(self.queue[self.queue_id].explaining_user,
                                          self.queue[self.queue_id].guessing_user, word, verdict, screen_time)
        self.pool = self.pool[1:]
        if not self.pool:
            self.status = 'show_stats'

    def endgame(self):
        self.last_statistics = PartyStatistics([], [])
        self.status = "game_setup"
        self.players = None
        self.word_dictionary = None
        self.settings = None
        self.pool = None
        self.queue = []
        self.queue_id = None
