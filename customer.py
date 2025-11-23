class Customer:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self._name
        
    @name.setter 
    def name(self,name):
        if not  isinstance(name,str) :
            raise ValueError("Name must be a string ")
        if not (1<= len(name.strip())<= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name=name
        pass
    pass

