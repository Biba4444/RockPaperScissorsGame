import unittest
import os
import tempfile
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.score_saver import ScoreHandler, GameRecord

class TestScoreSaver(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_dir = tempfile.mkdtemp()
        self.score_file = os.path.join(self.test_dir, "score.txt")
        self.score_handler = ScoreHandler()
        self.score_handler.file_name = self.score_file

    def test_add_record(self):
        """Test adding a new record."""
        game_record = GameRecord([], self.score_handler)
        game_record.add_record("TestPlayer", 100.0)
        
        with open(self.score_file, 'r') as file:
            content = file.read().strip()
            self.assertIn("TestPlayer: 100.0", content)

    def test_sort_records(self):
        """Test sorting records by score."""
        records = [
            ("Player1", 50.0),
            ("Player2", 100.0),
            ("Player3", 75.0)
        ]
        game_record = GameRecord(records, self.score_handler)
        sorted_records = game_record.sort_records()
        
        self.assertEqual(sorted_records[0][1], 100.0)
        self.assertEqual(sorted_records[-1][1], 50.0)

if __name__ == '__main__':
    unittest.main() 