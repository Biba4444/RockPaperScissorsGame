class GameOverException(Exception):
    """Exception raised when the game is over."""
    def __init__(self, message="Game Over!"):
        super().__init__(message)