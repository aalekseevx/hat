from random import shuffle

import config
from namedlist import namedlist

from statistics import PartyStatistics

PlayingPair = namedlist('PlayingPair', ['explaining_user', 'guessing_user'])


class GameController:
    def __init__(self) -> None:
        """GameController initialization"""
        self.global_statistics = PartyStatistics([], [])
        self.last_statistics = PartyStatistics([], [])

        self.status = "game_setup"
        self.players = None
        self.word_dictionary = None
        self.settings = None
        self.pool = None
        self.queue = []
        self.queue_id = None

    def start_game_(self, players: list, settings: dict) -> None:
        """Game start"""
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

    def start_round(self) -> None:
        """start new round"""
        self.status = "playing"
        shuffle(self.pool)

    def finish_round(self) -> None:
        """finish round"""
        if self.status != 'waiting_round':
            self.queue_id = (self.queue_id + 1) % len(self.queue)
            self.status = 'waiting_round'

    def remove_word(self, verdict: str, screen_time: float) -> None:
        """remove word and and update statistics"""
        word = self.pool[0]
        self.last_statistics.add_result(self.queue[self.queue_id].explaining_user,
                                        self.queue[self.queue_id].guessing_user, word, verdict, screen_time)
        self.global_statistics.add_result(self.queue[self.queue_id].explaining_user,
                                          self.queue[self.queue_id].guessing_user, word, verdict, screen_time)
        self.pool = self.pool[1:]
        if not self.pool:
            self.status = 'show_stats'

    def endgame(self) -> None:
        """endgame"""
        self.last_statistics = PartyStatistics([], [])
        self.status = "game_setup"
        self.players = None
        self.word_dictionary = None
        self.settings = None
        self.pool = None
        self.queue = []
        self.queue_id = None
