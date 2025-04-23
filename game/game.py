from models import Enemy, Player

class Game:
    def __init__(self, player, mode):
        self.player = Player(input("Enter your name: "))
        self.mode = mode
        self.enemy = Enemy("Default Enemy", 100, 10)
    
    def create_enemy(self):
        if self.mode == "easy":
            self.enemy = Enemy("Easy Enemy", 50, 5)
        elif self.mode == "medium":
            self.enemy = Enemy("Medium Enemy", 100, 10)
        elif self.mode == "hard":
            self.enemy = Enemy("Hard Enemy", 150, 15)
        else:
            raise ValueError("Invalid game mode")
    
    def fight(self):
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        
        if player_attack == enemy_attack:
            print("It's a tie!")
        elif (player_attack == "Rock" and enemy_attack == "Scissors") or \
             (player_attack == "Paper" and enemy_attack == "Rock") or \
             (player_attack == "Scissors" and enemy_attack == "Paper"):
            print("You win this round!")
            self.enemy.decrease_life()
        else:
            print("Enemy wins this round!")
            self.player.decrease_life()
        if self.player.lives == 0:
            return -1
        elif self.enemy.lives == 0:
            return 1
        else:
            return 0
        
    def handle_fight_result(self):
        if self.fight() == 1:
            print("Congratulations! You defeated the enemy.")
            self.player.add_score(10)
        elif self.fight() == -1:
            print("Unfortunately, you lost all your lives.")
            self.player.add_score(0)
            
    def play(self):
        self.create_enemy()
        while self.player.lives > 0 and self.enemy.lives > 0:
            self.fight()
        self.handle_fight_result()
        