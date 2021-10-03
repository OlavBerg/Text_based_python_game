from character import Character
from item import Item
from sword import Sword

class PlayerCharacter(Character):
    def __init__(self):
        super().__init__()
        self.inventory = []

    def getInventory(self):
        return self.inventory

    def putInInventory(self, item: Item):
        self.inventory.append(item)

    def equipSword(self, sword: Sword):
        try:
            self.inventory.remove(sword)
            self.equippedSword = sword
            return True
        except:
            return False
    
    def unequipSword(self):
        sword = self.equippedSword

        if sword == None:
            return False
        else:
            self.equippedSword = None
            self.putInInventory(sword)
            return True

    
