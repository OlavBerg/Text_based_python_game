from item import Item
from key import Key
from flashlight import Flashlight

class Inventory:
    def __init__(self):
        self.itemList = []

    def append(self, item: Item):
        self.itemList.append(item)

    def remove(self, item: Item):
        try:
            self.itemList.remove(item)
        except:
            pass

    def getItemsOfType(self, itemType: type):
        listOfItemsOfType = []

        for item in self.itemList:
            if isinstance(item, itemType):
                listOfItemsOfType.append(item)

        return listOfItemsOfType

    def getKey(self, color: str, shape: str):
        retrievedKey = None

        for key in self.getItemsOfType(Key):
            if key.getColor() == color and key.getShape() == shape:
                retrievedKey = key
                break

        return retrievedKey

    def getFlashlight(self):
        flashlight = None

        for item in self.itemList:
            if isinstance(item, Flashlight):
                flashlight = item
                break

        return flashlight

    def print(self):
        for item in self.itemList:
            if isinstance(item, Key):
                key = item
                color = key.getColor()
                shape = key.getShape()
                print("• " + color.capitalize() + " " + shape.lower() + " key")
            elif isinstance(item, Flashlight):
                print("• Flashlight")



#print("• " + color.capitalize() + " " + shape.lower())

    