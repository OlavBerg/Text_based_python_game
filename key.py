from item import Item

class Key(Item):
    def __init__(self, color: str, shape: str):
        super().__init__()
        self.color = color
        self.shape = shape

    def getColor(self):
        return self.color

    def getShape(self):
        return self.shape

    
