from game.models import Player, Enemy
from game import settings

class Game:
    def __init__(self, player, mode, level=1):
        if mode not in settings.MODES:
            raise ValueError(f"Invalid mode: {mode}")
        if not isinstance(level, (int, float)):
            raise TypeError(f"Expected 'level' to be int or float, got {type(level).__name__}")
        
        self.player = player
        self.mode = settings.MODES[mode]
        self.level = level
        self.enemy = None
    
    def create_enemy(self):
        hardness = settings.MODE_MULTIPLIERS[self.mode]
        self.enemy = Enemy(self.level, hardness)
    
    def fight(self):
        player_attack = self.player.select_attack()
        if player_attack is None:
            print("Player exited the game.")
            return
        
        enemy_attack = self.enemy.select_attack()
        outcome = settings.ATTACK_PAIRS_OUTCOME.get((player_attack, enemy_attack))
        
        score_for_fight = settings.POINTS_FOR_FIGHT * (self.level * settings.EACH_LEVEL_MULTIPLIER) * settings.MODE_MULTIPLIERS[self.mode]
        
        if outcome is None:
            print("Invalid attack pair.")
            return
        if outcome == settings.WIN:
            print("You win this round!")
            self.level += 1
            self.enemy.decrease_life()
            self.player.add_score(score_for_fight)
        elif outcome == settings.DRAW:
            print("It's a draw!")
        elif outcome == settings.LOSE:
            print("Enemy wins this round!")
            self.player.decrease_life()
    
    def handle_fight_result(self):
        score_for_killing = settings.POINTS_FOR_KILLING * (self.level * settings.EACH_LEVEL_MULTIPLIER) * settings.MODE_MULTIPLIERS[self.mode]
        if self.enemy.lives <= 0:
            print("Congratulations! You defeated the enemy.")
            self.player.add_score(score_for_killing)
        elif self.player.lives <= 0:
            print("Unfortunately, you lost all your lives.")
    
    def play(self):
        self.create_enemy()
        while self.player.lives > 0 and self.enemy.lives > 0:
            self.fight()
        self.handle_fight_result()