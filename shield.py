from item import Item

class Shield(Item):
    def __init__(self, protection: int):
        super().__init__()
        self.protection = protection

    def getProtection(self):
        return self.protection

    def upgrade(self):
        self.protection += 1
    
    def downgrade(self):
        self.protection -= 1

    def setProtection(self, protection: int):
        self.protection = protection
