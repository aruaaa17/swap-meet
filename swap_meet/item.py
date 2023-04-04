import uuid
class Item:
    
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
    
    def get_category(self):    
        return self.__class__.__name__
    
    