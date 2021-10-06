# Developed by Olav Berg

class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def isEqual(self, coordinates):
        return self.x == coordinates.getX() and self.y == coordinates.getY()

    def inList(self, coordinatesList: list):
        for coordinates in coordinatesList:

            if self.isEqual(coordinates):
                return True

        return False

    def removeFromList(self, coordinatesList: list):
        for i in len(coordinatesList):

            if self.isEqual(coordinatesList[i]):
                coordinatesList.pop(i)
                break

    def getNext(self, direction: str):
        "Returns the next coordinates in the given direction ('n', 'e', 's' or 'w')."

        if direction == "n":
            return Coordinates(self.x - 1, self.y)
        elif direction == "e":
            return Coordinates(self.x, self.y + 1)
        elif direction == "s":
            return Coordinates(self.x + 1, self.y)
        elif direction == "w":
            return Coordinates(self.x, self.y - 1)
        else:
            return None

    def update(self, direction: str):
        """Changes the coordinates one step in the given direction ('n', 'e', 's' or 'w')."""

        if direction == "n":
            self.x -= 1
        elif direction == "e":
            self.y += 1
        elif direction == "s":
            self.x += 1
        elif direction == "w":
            self.y -= 1
        else:
            pass

    def toString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"