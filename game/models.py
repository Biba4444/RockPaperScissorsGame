import random
import math
from game.exceptions import GameOverException, EnemyDownException
from game import settings
from game import score_saver

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = settings.PLAYER_LIVES
        self.score = 0
    
    def select_attack(self):
        while True:
            attack = input(f"{self.name}, choose your attack: 1 for Rock, 2 for Paper, 3 for Scissors (or type 'exit' to quit): ").strip()
            if attack.lower() == 'exit':
                print("Exiting attack selection.")
                return None
            if attack in settings.ALLOWED_ATTACKS:
                return settings.ALLOWED_ATTACKS[attack]
            print("Invalid choice. Please select again.")
        
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"{self.name} has no lives left!")
            raise GameOverException()
        
    def add_score(self, points):
        self.score += points
        score_handler = score_saver.ScoreHandler()
        records = score_handler.read_scores()
        game_record = score_saver.GameRecord(records)
        game_record.add_record(self.name, self.score)
        game_record.update_file()
            
class Enemy:
    def __init__(self, level, hardness):
        self.level = level
        self.hardness = hardness
        self.lives = math.floor(settings.PLAYER_LIVES * self.hardness * (self.level * settings.EACH_LEVEL_MULTIPLIER))
         
    def select_attack(self):
        attack = random.randint(1, 3)
        attack_str = str(attack)
        if attack_str in settings.ALLOWED_ATTACKS:
            return settings.ALLOWED_ATTACKS[attack_str]
        raise ValueError(f"Invalid attack generated: {attack}")
    
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"Enemy defeated!")
            raise EnemyDownException()