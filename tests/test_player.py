import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.models import Player
from game.exceptions import GameOverException
from game import settings

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.player = Player("TestPlayer")

    def test_player_initialization(self):
        """Test player initialization with valid name."""
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.lives, settings.PLAYER_LIVES)
        self.assertEqual(self.player.score, 0.0)

    def test_player_empty_name(self):
        """Test player initialization with empty name."""
        with self.assertRaises(ValueError):
            Player("")

    def test_player_whitespace_name(self):
        """Test player initialization with whitespace name."""
        with self.assertRaises(ValueError):
            Player("   ")

    def test_decrease_life(self):
        """Test decreasing player's life."""
        initial_lives = self.player.lives
        self.player.decrease_life()
        self.assertEqual(self.player.lives, initial_lives - 1)

    def test_decrease_life_game_over(self):
        """Test game over when lives reach zero."""
        self.player.lives = 1
        with self.assertRaises(GameOverException):
            self.player.decrease_life()

    def test_add_score(self):
        """Test adding score to player."""
        points = 10.0
        self.player.add_score(points)
        self.assertEqual(self.player.score, points)

    @patch('builtins.input', side_effect=['1'])
    def test_select_attack(self, mock_input):
        """Test attack selection."""
        attack = self.player.select_attack()
        self.assertEqual(attack, settings.ALLOWED_ATTACKS['1'])

    @patch('builtins.input', side_effect=['exit'])
    def test_select_attack_exit(self, mock_input):
        """Test attack selection with exit."""
        attack = self.player.select_attack()
        self.assertIsNone(attack)

    @patch('builtins.input', side_effect=['4', '1'])
    def test_select_attack_invalid_then_valid(self, mock_input):
        """Test invalid then valid attack selection."""
        attack = self.player.select_attack()
        self.assertEqual(attack, settings.ALLOWED_ATTACKS['1'])

if __name__ == '__main__':
    unittest.main() 