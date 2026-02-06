from game import *

def main():
    game_name = input("Enter the Game you are playing: ").lower()
    game = get_dic(game_name)
    if game is None:
        print(f"{game_name} not found")
        quit()
    player_count = get_player_count()
    setup_time_input = input("do you want to know the setup time (y/n)").lower().strip() in ("y")
    rule = get_rule(game_name, player_count)
    setup_time = get_setup_time(game , setup_time_input)
    print(f"{rule}")
    if setup_time_input == True:
        print(f"{setup_time}")

def get_rule(game_name: str , player_count: int):
    for game in Game:
        if game.game_name == game_name:
            return game.player_count_to_rule.get(player_count, None)
    return None

def get_dic(game_name: str):
    for game in Game:
        if game.game_name == game_name:
            return game
    return None

def get_setup_time(game: Game , setup_time_input: bool):
    if setup_time_input == True:
        return game.setup_time
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


main()
