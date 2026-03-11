class SearchService:       
    def __init__(self, notes): 
        self.notes = notes 
    
    def search_by_title(self, query):
        filtered_notes = list(filter(lambda note: query.lower() in note.title.lower(), self.notes))
        return filtered_notes
    
    def search_by_content(self, query): 
        filtered_notes = list(filter(lambda note: query.lower() in note.content.lower(), self.notes))
        return filtered_notes 
    
    def search_by_tag(self, tag): 
        filtered_notes = [note for note in self.notes if tag in note.tags] 
        return filtered_notes  
    
    