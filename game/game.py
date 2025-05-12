from game.models import Player, Enemy
from game import settings
from game.exceptions import GameOverException, EnemyDownException

class Game:
    player: Player
    mode: str
    level: float
    enemy: Enemy

    def __init__(self, player: Player, mode: str, level: float = 1) -> None:
        if mode not in settings.MODES:
            raise ValueError(f"Invalid mode: {mode}")
        if not isinstance(level, (int, float)):
            raise TypeError(f"Expected 'level' to be int or float, got {type(level).__name__}")
        
        self.player = player
        self.mode = settings.MODES[mode]
        self.level = level
        self.enemy = None
    
    def create_enemy(self) -> None:
        hardness: float = settings.MODE_MULTIPLIERS[self.mode]
        self.enemy = Enemy(int(self.level), hardness)
    
    def fight(self) -> None:
        try:
            if self.enemy is None:
                raise ValueError("Enemy not created")

            player_attack: str = self.player.select_attack()
            if player_attack is None:
                print("Player exited the game.")
                return
            
            enemy_attack: str = self.enemy.select_attack()
            outcome: int = settings.ATTACK_PAIRS_OUTCOME.get((player_attack, enemy_attack))
            
            score_for_fight: float = settings.POINTS_FOR_FIGHT * (self.level * settings.EACH_LEVEL_MULTIPLIER) * settings.MODE_MULTIPLIERS[self.mode]
            
            if outcome is None:
                print("Invalid attack pair.")
                return
            
            print(f"Player chose: {player_attack}")
            print(f"Enemy chose: {enemy_attack}")
            
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
                
        except (GameOverException, EnemyDownException) as e:
            raise
        except Exception as e:
            print(f"An error occurred during the fight: {str(e)}")
    
    def handle_fight_result(self) -> None:
        try:
            if self.enemy is None:
                raise ValueError("Enemy not created")

            score_for_killing: float = settings.POINTS_FOR_KILLING * (self.level * settings.EACH_LEVEL_MULTIPLIER) * settings.MODE_MULTIPLIERS[self.mode]
            if self.enemy.lives <= 0:
                print("Congratulations! You defeated the enemy.")
                self.player.add_score(score_for_killing)
            elif self.player.lives <= 0:
                print("Unfortunately, you lost all your lives.")
        except Exception as e:
            print(f"An error occurred while handling fight result: {str(e)}")
    
    def play(self) -> None:
        try:
            self.create_enemy()
            print(f"\nStarting game at level {self.level}")
            print(f"Mode: {self.mode}")
            print(f"Enemy lives: {self.enemy.lives}")
            print(f"Your lives: {self.player.lives}\n")
            
            while self.player.lives > 0 and self.enemy and self.enemy.lives > 0:
                print(f"\nLevel {self.level}")
                print(f"Your lives: {self.player.lives} | Enemy lives: {self.enemy.lives}")
                self.fight()
            self.handle_fight_result()
        except (GameOverException, EnemyDownException):
            self.handle_fight_result()
        except Exception as e:
            print(f"An error occurred during the game: {str(e)}")