from sword import Sword
from shield import Shield

class Character:
    def __init__(self, strength: int = 1, equippedSword: Sword = None, 
        equippedShield: Shield = None):

        self.strength = strength
        self.equippedSword = equippedSword
        self. equippedShield = equippedShield

    def getStrength(self):
        return self.strength

    def getEquippedSword(self):
        return self.equippedSword

    def getEquippedShield(self):
        return self.equippedShield

    def powerUp(self):
        self.strength += 1
    
    def powerDown(self):
        if self.strength > 0:
            self.strength -= 1
            return True
        else:
            return False

    def setStrength(self, strength: int):
        self.strength = strength
