import uuid 
import time 

class Note: 
    def __init__(self, title, content, id=None, tags=None, rating=0.0, created_at=None, updated_at=None): 
        self.id = id if id else str(uuid.uuid4())
        self.title = title 
        self.content = content
        self.tags = tags if tags is not None else [] 
        self.rating = rating 
        self.created_at = created_at if created_at else self.get_timestamp()
        self.updated_at = updated_at if updated_at else self.get_timestamp()
        
    def add_tag(self, tag): 
        if tag not in self.tags: 
            self.tags.append(tag)
            self.updated_at = self.get_timestamp()
            return 
        
    def remove_tag(self, tag): 
        if tag in self.tags: 
            self.tags.remove(tag)
            self.updated_at = self.get_timestamp()
            return 
    
    def update_content(self, new_content): 
        self.content = new_content
        self.updated_at = self.get_timestamp()
        return

    def set_rating(self, new_rating): 
        self.rating = new_rating 
        self.updated_at = self.get_timestamp()
        return 
        
    @staticmethod
    def get_timestamp(): 
        return time.ctime()
    
    def to_dict(self): 
        return {
            "id": self.id, 
            "title": self.title, 
            "content": self.content,
            "tags": self.tags, 
            "rating": self.rating, 
            "created_at": self.created_at, 
            "updated_at": self.updated_at
        }
        
    @classmethod 
    def from_dict(cls, data): 
        return cls(**data)
    
    def __str__(self): 
        return f"Note: {self.title}, [{self.updated_at}]"
    
    def __repr__(self): 
        return f"Note(id={self.id}, title={self.title!r}, content={self.content!r}, \
                tags={self.tags}, rating={self.rating}, created_at={self.created_at}, updated_at={self.updated_at})"
                
    
    