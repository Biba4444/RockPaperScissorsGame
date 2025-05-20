import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.models import Enemy
from game.exceptions import EnemyDownException
from game import settings

class TestEnemy(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.level = 1
        self.hardness = 1.0
        self.enemy = Enemy(self.level, self.hardness)

    def test_enemy_initialization(self):
        """Test enemy initialization with valid parameters."""
        self.assertEqual(self.enemy.level, self.level)
        self.assertEqual(self.enemy.hardness, self.hardness)
        expected_lives = int(settings.PLAYER_LIVES * self.hardness * (self.level * settings.EACH_LEVEL_MULTIPLIER))
        self.assertEqual(self.enemy.lives, expected_lives)

    def test_enemy_invalid_level(self):
        """Test enemy initialization with invalid level."""
        with self.assertRaises(ValueError):
            Enemy(0, self.hardness)

    def test_enemy_invalid_hardness(self):
        """Test enemy initialization with invalid hardness."""
        with self.assertRaises(ValueError):
            Enemy(self.level, 0)

    def test_decrease_life(self):
        """Test decreasing enemy's life."""
        initial_lives = self.enemy.lives
        self.enemy.decrease_life()
        self.assertEqual(self.enemy.lives, initial_lives - 1)

    def test_decrease_life_enemy_down(self):
        """Test enemy down when lives reach zero."""
        self.enemy.lives = 1
        with self.assertRaises(EnemyDownException):
            self.enemy.decrease_life()

    def test_select_attack(self):
        """Test enemy attack selection."""
        attack = self.enemy.select_attack()
        self.assertIn(attack, settings.ALLOWED_ATTACKS.values())

    def test_enemy_lives_calculation(self):
        """Test enemy lives calculation with different levels and hardness."""
        test_cases = [
            (1, 1.0),
            (2, 1.0),
            (1, 2.0),
            (3, 1.5),
        ]
        
        for level, hardness in test_cases:
            enemy = Enemy(level, hardness)
            expected_lives = int(settings.PLAYER_LIVES * hardness * (level * settings.EACH_LEVEL_MULTIPLIER))
            self.assertEqual(enemy.lives, expected_lives)

if __name__ == '__main__':
    unittest.main() 