class Coffee:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not isinstance (name,str):
            raise ValueError("  Coffee name must be a string")
        if len (name.strip() < 3):
            raise ValueError(" Coffee name must be at lest 3 characters long")
        self._name=name


       
pass