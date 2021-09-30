from item import Item

class Sword(Item):
    def __init__(self, sharpness: int):
        super().__init__()
        self.sharpness = sharpness

    def getSharpness(self):
        return self.sharpness