import os
from game import settings

class ScoreHandler:
    def __init__(self):
        self.file_name = os.path.join(os.path.dirname(__file__), "score", "score.txt")
        self.game_records = []
        
    def read_scores(self):
        if not os.path.exists(self.file_name):
            print("Score file not found. Creating a new one.")
            return []
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line or ': ' not in line:  # Пропускаем строки без разделителя ": "
                    continue
                try:
                    name, score = line.split(': ')
                    self.game_records.append((name, float(score)))
                except ValueError:
                    print(f"Skipping invalid line: {line}")
        return self.game_records

class GameRecord:
    def __init__(self, records, score_handler):
        self.records = records
        self.score_handler = score_handler

    def add_record(self, name, score):
        # Проверяем, существует ли имя в текущих записях
        for i, (existing_name, existing_score) in enumerate(self.records):
            if existing_name == name:
                # Обновляем счёт, если имя найдено
                self.records[i] = (name, existing_score + score)  # Суммируем старый и новый счёт
                break
        else:
            # Добавляем новую запись, если имя не найдено
            self.records.append((name, score))
        self.update_file()  # Сохраняем изменения в файл
        
    def sort_records(self):
        if not self.records:
            print("No records to sort.")
            return []
        self.records.sort(key=lambda x: x[1], reverse=True)  # Сортировка по убыванию очков
        return self.records
        
    def update_file(self):
        sorted_records = self.sort_records()
        with open(self.score_handler.file_name, 'w') as file:
            for name, score in sorted_records:
                file.write(f"{name}: {score}\n")