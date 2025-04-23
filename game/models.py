import random
import math
from exceptions import GameOverException, EnemyDownException
import settings

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = settings.PLAYER_LIVES
        self.score = 0
    
    def select_attack(self):
        while True:
            try:
                attack = input(f"{self.name}, choose your attack: 1 for Rock, 2 for Paper, 3 for Scissors: ")
                if attack in settings.ALLOWED_ATTACKS:
                    return settings.ALLOWED_ATTACKS[attack]
                else:
                    print("Invalid choice. Please select again.")
            except Exception as e:
                print(f"An error occurred: {e}")
        
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"{self.name} has no lives left!")
            raise GameOverException()
        
    def add_score(self, points):
        self.score += points
        with open("./score/score.txt", "w") as file:
            file.write(f"{self.name}: {self.score} points\n")
            
class Enemy:
    def __init__(self, level, hardness):
        self.level = level
        self.hardness = hardness
        self.lives = math.floor(settings.PLAYER_LIVES * self.hardness * (self.level * settings.EACH_LEVEL_MULTIPLIER))
         
    def select_attack(self):
        attack = random.randint(1, 3)
        attack_str = str(attack)
        return settings.ALLOWED_ATTACKS.get(attack_str, "Unknown Attack")
    
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"Enemy defeated!")
            raise EnemyDownException()