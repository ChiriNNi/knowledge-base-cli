import json
import os  
import shutil
from pathlib import Path 
from models.note import Note

class Storage: 
    def __init__(self, file_path="data/notes.json"): 
        self.notes = [] 
        self.file_path = Path(file_path)
    
    def load_notes(self): 
        try: 
            with open(self.file_path, "r", encoding="utf-8") as file: 
                self.notes = [Note.from_dict(data) for data in json.load(file)]
                return self.notes 
        except (FileNotFoundError, json.JSONDecodeError): 
            self.notes = []
            return self.notes 
        
    def save_notes(self, note: Note): 
        self.notes.append(note)
        
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        with open(self.file_path, "w", encoding="utf-8") as file: 
            json.dump(
                [note.to_dict() for note in self.notes], 
                file, 
                indent=4, 
                ensure_ascii=False
            )
    
    def backup(self):
        if self.file_path.exists(): 
            return "Error: Main file didn't create. No backup."
        
        backup_path = self.file_path.with_stem(self.file_path.stem + "_backup")
        shutil.copy(self.file_path, backup_path)