class GameOverException(Exception):
    """Exception raised when the game is over."""
    def __init__(self, message="Game Over!"):
        super().__init__(message)
        
class EnemyDownException(Exception):
    """Exception raised when an enemy is down."""
    def __init__(self, message="Enemy is down!"):
        super().__init__(message)