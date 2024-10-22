from base import Base

class User(Base):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'name':
                name = value
            elif key == 'age':
                age = value
            elif key == 'id':
                id = value
            elif key == 'genero':
                self.genero = value
            else:
                self.__setattr__(key, value)
        try:
            super().__init__(name, age, id)
        except:
            raise Exception("\n\n\t-->Fail connecting to parent!\n\n")
            
#temp = User(name="Jose", age=37, id="Ejhdt571ga4jkai")
