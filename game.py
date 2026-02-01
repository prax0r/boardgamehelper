from enum import Enum


class Rule(Enum):
    UNO_TWO_PLAYERS = "Mische alle 108 Karten und zieht jeweils 10 Karten"
    UNO_THREE_TWELVE_PLAYERS = "Mische alle 108 Karten und zieht jeweils 7 Karten"
    DUNE_ONE_PLAYER = "Dune ein spieler"
    DUNE_TWO_PLAYERS = "Dune zwei spieler"
    DUNE_THREE_FOUR_PLAYERS = "Dune 3-4 spieler"
    
class Game(Enum):
    UNO = ("uno", {2: Rule.UNO_TWO_PLAYERS.value , **{n: Rule.UNO_THREE_TWELVE_PLAYERS.value for n in range (3, 12)}})
    DUNE = ("dune", {1: Rule.DUNE_ONE_PLAYER.value , 2: Rule.DUNE_TWO_PLAYERS.value , **{n: Rule.DUNE_THREE_FOUR_PLAYERS.value for n in range (3, 4)}})
           
    def __init__(self, game_name: str, player_count_to_rule: dict[int, str]):
        self.game_name = game_name
        self.player_count_to_rule = player_count_to_rule
