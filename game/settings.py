"""Game settings and constants."""

# Game modes
MODE_NORMAL: str = 'Normal'
MODE_HARD: str = 'Hard'
MODES: dict = {
    '1': MODE_NORMAL,
    '2': MODE_HARD
}
MODE_MULTIPLIERS: dict = {
    MODE_NORMAL: 1,
    MODE_HARD: 2
}

# Player settings
PLAYER_LIVES: int = 2

# Scoring
POINTS_FOR_FIGHT: float = 1
POINTS_FOR_KILLING: float = 5
MAX_RECORDS_NUMBER: int = 5
EACH_LEVEL_MULTIPLIER: float = 1.5

# File settings
SCORE_FILE: str = 'score.txt'

# Attack types
ROCK: str = 'Rock'
PAPER: str = 'Paper'
SCISSORS: str = 'Scissors'

# Game outcomes
WIN: int = 1
DRAW: int = 0
LOSE: int = -1

# Attack mappings
ALLOWED_ATTACKS: dict = {
    '1': ROCK,
    '2': PAPER,
    '3': SCISSORS
}

# Attack outcomes matrix
ATTACK_PAIRS_OUTCOME: dict = {
    (ROCK, ROCK): DRAW,
    (ROCK, PAPER): LOSE,
    (ROCK, SCISSORS): WIN,
    (PAPER, ROCK): WIN,
    (PAPER, PAPER): DRAW,
    (PAPER, SCISSORS): LOSE,
    (SCISSORS, ROCK): LOSE,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, SCISSORS): DRAW
}