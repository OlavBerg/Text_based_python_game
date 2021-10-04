from item import Item

class Sword(Item):
    def __init__(self, sharpness: int):
        super().__init__()
        self.sharpness = sharpness

    def getSharpness(self):
        return self.sharpness

    def upgrade(self):
        self.sharpness += 1

    def downgrade(self):
        self.sharpness -= 1

    def setSharpness(self, sharpness: int):
        self.sharpness = sharpness