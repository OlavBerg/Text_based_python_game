from key import Key


class Door: 
    def __init__(self, initiallyLocked: bool, color: str = None, shape: str = None):
        self.locked = initiallyLocked
        self.color = color
        self.shape = shape

    def isLocked(self):
        return self.locked

    def getColor(self):
        return self.color

    def getShape(self):
        return self.shape

    def unlock(self, key: Key):
        """If the given key matches the color and shape of the door, 
        the door unlocks and True is returned. Otherwise False is returned."""

        if self.color == key.color and self.shape == key.shape :
            self.locked = False
            return True

    def setColor(self, color: str):
        pass

    def setShape(self, shape: str):
        pass
        
