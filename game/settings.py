"""Game settings and constants."""

# Game modes
MODE_NORMAL = 'Normal'
MODE_HARD = 'Hard'
MODES = {
    '1': MODE_NORMAL,
    '2': MODE_HARD
}
MODE_MULTIPLIERS = {
    MODE_NORMAL: 1,
    MODE_HARD: 2
}

# Player settings
PLAYER_LIVES = 2

# Scoring
POINTS_FOR_FIGHT = 1
POINTS_FOR_KILLING = 5
MAX_RECORDS_NUMBER = 5
EACH_LEVEL_MULTIPLIER = 1.5

# File settings
SCORE_FILE = 'score.txt'

# Attack types
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

# Game outcomes
WIN = 1
DRAW = 0
LOSE = -1

# Attack mappings
ALLOWED_ATTACKS = {
    '1': ROCK,
    '2': PAPER,
    '3': SCISSORS
}

# Attack outcomes matrix
ATTACK_PAIRS_OUTCOME = {
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