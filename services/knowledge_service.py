from storage.storage_manager import Storage
from models.note import Note

class KnowledgetService:     
    def __init__(self): 
        self.storage = Storage()
        self.notes = self.storage.load_notes()
        
    def create_note(self, title, content): 
        note = Note(title, content)
        self.notes.append(note)
        self.storage.save_notes()
    
    def delete_note(self, note): 
        if note in self.notes: 
            self.notes.remove(note)
            self.storage.save_notes()
    
    def update_note(self, note_id, new_content): 
        for note in self.notes: 
            if note.id == note_id: 
                note.update_content(new_content)
                self.storage.save_notes()

    def get_note(self, note_id): 
        for note in self.notes: 
            if note.id == note_id: 
                return note 
    
    def list_notes(self): 
        return self.notes