import uuid
class Base:
    """Id is not needed"""
    def __init__(self, name, age, id):
        """id is not needed"""
        self.name = name
        self.age = age
        if not id:
            self._id = uuid.uuid4()
        else:
            self._id = id
    
    def save(self):
        pass
    
    def to_dict(self):
        return self.__dict__.copy()
    
    def delete(self):
        pass