from namedlist import namedlist

UserInfo = namedlist('UserInfo', ['username', ('guesses', 0), ('explanations', 0), ('mistakes', 0), ('points', 0)])
WordInfo = namedlist('WordInfo', ['word', ('screen_time', 0), ('tries', 0), ('mistake', False)])


class PartyStatistics:

    def add_objects(self, users, words):
        self.user_statistics.update({user: UserInfo(user, 0, 0, 0, 0) for user in users if user not in self.inside})
        self.inside.update(users)
        self.words_statistics.update({word: WordInfo(word=word) for word in words})

    def __init__(self, users, words):
        self.inside = set()
        self.user_statistics = {}
        self.words_statistics = {}
        self.add_objects(users, words)

    def add_result(self, explaining_user, guessing_user, word, verdict, screen_time):
        if verdict == 'correct':
            self.user_statistics[explaining_user].explanations += 1
            self.user_statistics[guessing_user].guesses += 1
            for user in [explaining_user, guessing_user]:
                self.user_statistics[user].points += 1
        elif verdict == 'mistake':
            self.words_statistics[word].mistake = True
            self.user_statistics[explaining_user].mistakes += 1
            self.user_statistics[explaining_user].points -= 1
        self.words_statistics[word].screen_time += screen_time
        self.words_statistics[word].tries += 1

    def get(self):
        return {
            'users': tuple(sorted([dict(user_info._asdict()) for user_info in self.user_statistics.values()],
                                  key=lambda x: x['points'], reverse=True))
            ,
            'words': tuple(sorted([dict(words_info._asdict()) for words_info in self.words_statistics.values()],
                                  key=lambda x: (x['tries'], x['screen_time']), reverse=True))
        }
