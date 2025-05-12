import random
import math
from game.exceptions import GameOverException, EnemyDownException
from game import settings
from game import score_saver

class Player:
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Player name cannot be empty")
        self.name = name.strip()
        self.lives = settings.PLAYER_LIVES
        self.score = 0
    
    def select_attack(self):
        print("\nAvailable attacks:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("Type 'exit' to quit")
        
        while True:
            try:
                attack = input(f"\n{self.name}, choose your attack: ").strip().lower()
                if attack == 'exit':
                    print("Exiting attack selection.")
                    return None
                if attack not in settings.ALLOWED_ATTACKS:
                    print("Invalid choice. Please select 1, 2, or 3.")
                    continue
                return settings.ALLOWED_ATTACKS[attack]
            except Exception as e:
                print(f"Error during attack selection: {str(e)}")
                print("Please try again.")
        
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"{self.name} has no lives left!")
            raise GameOverException()
        print(f"{self.name} has {self.lives} lives remaining.")
        
    def add_score(self, points):
        try:
            self.score += points
            print(f"{self.name} earned {points} points! Total score: {self.score}")
            
            score_handler = score_saver.ScoreHandler()
            records = score_handler.read_scores()
            game_record = score_saver.GameRecord(records, score_handler)
            game_record.add_record(self.name, self.score)
        except Exception as e:
            print(f"Error saving score: {str(e)}")
                
class Enemy:
    def __init__(self, level, hardness):
        if level < 1:
            raise ValueError("Level must be at least 1")
        if hardness <= 0:
            raise ValueError("Hardness must be positive")
            
        self.level = level
        self.hardness = hardness
        self.lives = math.floor(settings.PLAYER_LIVES * self.hardness * (self.level * settings.EACH_LEVEL_MULTIPLIER))
         
    def select_attack(self):
        try:
            attack = str(random.randint(1, 3))
            if attack not in settings.ALLOWED_ATTACKS:
                raise ValueError(f"Invalid attack generated: {attack}")
            return settings.ALLOWED_ATTACKS[attack]
        except Exception as e:
            print(f"Error during enemy attack selection: {str(e)}")
            # Return a default attack in case of error
            return settings.ALLOWED_ATTACKS['1']
    
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print("Enemy defeated!")
            raise EnemyDownException()
        print(f"Enemy has {self.lives} lives remaining.")