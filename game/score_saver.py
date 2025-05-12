import os
from game import settings

class ScoreHandler:
    """Handles reading and writing game scores to file."""
    file_name: str
    game_records: list

    def __init__(self) -> None:
        """Initialize score handler with empty records."""
        self.file_name = os.path.join(os.path.dirname(__file__), "score", "score.txt")
        self.game_records = []
        
    def read_scores(self) -> list:
        """Read and parse scores from file."""
        if not os.path.exists(self.file_name):
            print("Score file not found. Creating a new one.")
            return []
        
        with open(self.file_name, 'r') as file:
            lines: list = file.readlines()
            for line in lines:
                line = line.strip()
                if not line or ': ' not in line:
                    continue
                try:
                    name, score_str = line.split(': ')
                    self.game_records.append((name, float(score_str)))
                except ValueError:
                    print(f"Skipping invalid line: {line}")
        return self.game_records

class GameRecord:
    """Manages game records and their sorting."""
    records: list
    score_handler: ScoreHandler

    def __init__(self, records: list, score_handler: ScoreHandler) -> None:
        """Initialize with existing records and handler."""
        self.records = records
        self.score_handler = score_handler

    def add_record(self, name: str, score: float) -> None:
        """Add or update player's score."""
        for i, (existing_name, existing_score) in enumerate(self.records):
            if existing_name == name:
                self.records[i] = (name, existing_score + score)
                break
        else:
            self.records.append((name, score))
        self.update_file()
        
    def sort_records(self) -> list:
        """Sort records by score in descending order."""
        if not self.records:
            print("No records to sort.")
            return []
        self.records.sort(key=lambda x: x[1], reverse=True)
        return self.records
        
    def update_file(self) -> None:
        """Save sorted records to file."""
        sorted_records: list = self.sort_records()
        with open(self.score_handler.file_name, 'w') as file:
            for name, score in sorted_records:
                file.write(f"{name}: {score}\n")