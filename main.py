from game.models import Player
from game import game
from game import score_saver


def user_menu():
    user_choice = input("To start game press 1, to see results press 2, to leave the game press 3: ").strip().lower()
    return user_choice

def play_game():
    game_mode = input("Choose game mode: 1 for Easy, 2 for Hard : ").strip()
    if game_mode in ["1", "2"]:
        game_instance = game.Game(player=create_player(),mode=game_mode)
        game_instance.play()
    else:
        print("Invalid game mode selected.")
        
def create_player():
    player_name = input("Enter your name: ").strip()
    return Player(player_name)

def show_records():
    score_handler = score_saver.ScoreHandler()
    records = score_handler.read_scores()
    if records:
        print("Game Records:")
        for name, score in records:
            print(f"{name}: {score}")
    else:
        print("No game records found.")
        
def main():
    while True:
        match user_menu():
            case "1":
                play_game()
            case "2":
                show_records()
            case "3":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    