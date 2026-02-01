from game import *

def get_rule(game_name: str, player_count: int):
    for game in Game:
        if game.game_name == game_name:
            return game.player_count_to_rule.get(player_count, None)
    return None

def get_player_count():
    while True:
        player_count = input("How many players are playing: ")

        try:
            player_count = int(player_count)

            if player_count > 0:
                return player_count
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


game_name = input("Enter the Game you are playing: ").lower()
player_count = get_player_count()
rule = get_rule(game_name, player_count)
print(f"{rule}")

