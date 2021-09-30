from item import Item

class Shield(Item):
    def __init__(self, protection: int):
        super().__init__()
        self.protection = protection

    def getProtection(self):
        return self.protection
