from character import Character
from sword import Sword
from shield import Shield
from item import Item

class Enemy(Character):
    def __init__(self, strength: int, equippedSword: Sword, equippedShield: Shield, drops: list[Item]):
        super().__init__(strength, equippedSword, equippedShield)
        self.drops = drops

    def getDrops(self):
        return self.drops