from game import GameController


class Room(GameController):
    def __init__(self, name: str, username: str, lang: str):
        super().__init__()
        self.name = name
        self.lang = lang
        self.members = {
            username: "online"
        }

    def online(self):
        return [x[0] for x in self.members.items() if x[1] == 'online']

    def start_game(self, settings: dict):
        self.start_game_(self.online(), settings)

    def get_broadcast_data(self):
        broadcast_keys = [
            'name',
            'lang',
            'status',
            'pool',
            'settings',
            'members',
            'queue_id',
            'players',
        ]
        return {
            **{key: self.__dict__[key] for key in broadcast_keys},
            **{
                "global_statistics": self.global_statistics.get(),
                "last_statistics": self.last_statistics.get(),
                "queue": [tuple(pair) for pair in self.queue]
            }
        }

    def make_offline(self, username):
        self.members[username] = "offline"

    def join(self, username):
        self.members[username] = "online"

    def leave(self, username):
        self.members[username] = "offline"
