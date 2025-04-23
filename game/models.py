import random
from exceptions import GameOverException, EnemyDownException

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = lives
        self.score = 0
    
    def select_attack(self, attack):
        while True:
            try:
                input(f"{self.name}, choose your attack: 1 for Rock, 2 for Paper, 3 for Scissors: ")
                if attack == 1:
                    return "Rock"
                elif attack == 2:
                    return "Paper"
                elif attack == 3:
                    return "Scissors"
                else:
                    print("Invalid choice. Please select again.")
                    return self.select_attack(attack)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
           
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOverException()
        
    def add_score(self, points):
        self.score += points
        with open("./score/score.txt", "w") as file:
            file.write(f"{self.name}: {self.score} points\n")
            
class Enemy:
    def __init__(self, level, hardness):
        self.level = level
        self.hardness = hardness
        self.lives = lives
         
    def select_attack(self):
        attack = random.randint(1, 3)
        if attack == 1:
            return "Rock"
        elif attack == 2:
            return "Paper"
        elif attack == 3:
            return "Scissors"
    
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDownException()
        
        