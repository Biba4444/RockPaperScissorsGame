import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.game import Game
from game.models import Player
from game import settings

class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = Player("TestPlayer")
        self.game = Game(self.player, "1", 1.0)

    def test_game_initialization(self):
        """Test game initialization with valid parameters."""
        self.assertEqual(self.game.player, self.player)
        self.assertEqual(self.game.mode, settings.MODES["1"])
        self.assertEqual(self.game.level, 1.0)
        self.assertIsNone(self.game.enemy)

    def test_create_enemy(self):
        """Test enemy creation."""
        self.game.create_enemy()
        self.assertIsNotNone(self.game.enemy)
        self.assertEqual(self.game.enemy.level, int(self.game.level))
        self.assertEqual(self.game.enemy.hardness, settings.MODE_MULTIPLIERS[self.game.mode])

    @patch('game.models.Player.select_attack')
    @patch('game.models.Enemy.select_attack')
    def test_fight_player_win(self, mock_enemy_attack, mock_player_attack):
        """Test fight outcome when player wins."""
        mock_player_attack.return_value = settings.ROCK
        mock_enemy_attack.return_value = settings.SCISSORS
        self.game.create_enemy()
        initial_score = self.player.score
        self.game.fight()
        self.assertGreater(self.player.score, initial_score)

if __name__ == '__main__':
    unittest.main() 