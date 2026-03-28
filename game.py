import enum


class Rule(enum.Enum):
    UNO_TWO_PLAYERS = "Shuffle all 108 cards, every player draws 10 cards."
    UNO_THREE_TWELVE_PLAYERS = "Shuffle all 108 cards, every player draws 7 cards."
    DUNE_ONE_PLAYER = "Why are you playing alone"
    DUNE_TWO_PLAYERS = "Dune with two players"
    DUNE_THREE_FOUR_PLAYERS = "dune with four players"
    
class Game(enum.Enum):
    UNO = ("uno", "1 hour" ,  {2: Rule.UNO_TWO_PLAYERS.value , **{n: Rule.UNO_THREE_TWELVE_PLAYERS.value for n in range (3, 12)}})
    DUNE = ("dune", "1 hour" , {1: Rule.DUNE_ONE_PLAYER.value , 2: Rule.DUNE_TWO_PLAYERS.value , **{n: Rule.DUNE_THREE_FOUR_PLAYERS.value for n in range (3, 4)}})
           
    def __init__(self, game_name: str, setup_time: str , player_count_to_rule: dict[int, str]):
        self.game_name = game_name
        self.player_count_to_rule = player_count_to_rule
        self.setup_time = setup_time
