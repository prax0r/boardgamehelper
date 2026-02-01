from enum import Enum


class Rule(Enum):
    UNO_TWO_FOUR_PLAYERS = "Regeln example"
    
class Game(Enum):
    UNO = ("Uno", {2: Rule.UNO_TWO_FOUR_PLAYERS.value , 3: Rule.UNO_TWO_FOUR_PLAYERS.value})
    def __init__(self, game_name: str, player_count_to_rule: dict[int, str]):
        self.game_name = game_name
        self.player_count_to_rule = player_count_to_rule
