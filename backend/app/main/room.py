from .game import GameController
from typing import Dict, Any, List


class Room(GameController):
    def __init__(self, name: str, username: str, lang: str) -> None:
        """Room initialization """
        super().__init__()
        self.name = name
        self.lang = lang
        self.members = {
            username: "online"
        }

    def online(self) -> List[str]:
        """return online users"""
        return [x[0] for x in self.members.items() if x[1] == 'online']

    def start_game(self, settings: dict) -> None:
        """prepare settings and users to start"""
        self.start_game_(self.online(), settings)

    def get_broadcast_data(self) -> Dict[str, Any]:
        """return all possible data from room"""
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

    def make_offline(self, username: str) -> None:
        """make user offline"""
        self.members[username] = "offline"

    def join(self, username: str) -> None:
        """user join"""
        self.members[username] = "online"

    def leave(self, username: str) -> None:
        """user leave"""
        self.members[username] = "offline"
