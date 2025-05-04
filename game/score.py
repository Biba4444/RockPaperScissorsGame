import os
import settings

class ScoreHandler:
    def __init__(self, file_name=settings.SCORE_FILE):
        self.file_name = os.path.join(os.path.dirname(__file__), file_name)
        self.game_records = []
        
    def read_scores(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, score = line.strip().split(',')
                self.game_records.append((name, int(score)))
            return self.game_records

class GameRecord:
    def __init__(self, records):
        self.records = records

    def add_record(self, name, score):
        self.records = ScoreHandler().read_scores()
        self.records.append((name, score))
        
    def sort_records(self):
        if not self.records:
            print("No records to sort.")
            return []
        self.records.sort(key=lambda x: x[1], reverse=True)
        return self.records[:settings.MAX_RECORDS_NUMBER]
        
    def save_records(self):
        with open(ScoreHandler().file_name, 'w') as file:
            for name, score in self.records:
                file.write(f"{name},{score}\n")
                
    def update_file(self):
        sorted_records = self.sort_records()
        with open(ScoreHandler().file_name, 'w') as file:
            for name, score in sorted_records:
                file.write(f"{name},{score}\n")
    

class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score
    
    def __gt__(self, other):
        return self.score > other.score
    
    def __str__(self):
        return f"{self.name} - {self.mode} - {self.score}"