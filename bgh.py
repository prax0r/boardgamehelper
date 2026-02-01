

GameName = input("Enter the Game you are playing: ")

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

PlayerCount = get_player_count()
print(f"Player Count is, {PlayerCount}")
