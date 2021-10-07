# Developed by Olav Berg

from room import Room
from coordinates import Coordinates

class RoomMatrix:
    """A 2-dimensional array of rooms."""

    def __init__(self, numOfRows: int, numOfColumns: int):
        self.matrix = [] # A double list countaining rooms.

        for x in range(numOfRows):
            row = []

            for y in range(numOfColumns):
                row.append(None)
            
            self.matrix.append(row)

        self.numOfRows = numOfRows
        self.numOfColumns = numOfColumns

    def getNumOfRows(self):
        return self.numOfRows

    def getNumOfColumns(self):
        return self.numOfColumns

    def validCoordinates(self, coordinates: Coordinates):
        
        x = coordinates.getX()
        y = coordinates.getY()

        return x >= 0 and x <= self.numOfRows - 1 and y >= 0 and y <= self.numOfColumns - 1

    def getRoom(self, coordinates: Coordinates):

        if self.validCoordinates(coordinates):
            return self.matrix[coordinates.getX()][coordinates.getY()]
        else:
            return None

    def placeRoom(self, room: Room, coordinates: Coordinates):
        if self.validCoordinates(coordinates):
            self.matrix[coordinates.getX()][coordinates.getY()] = room
            return True
        else:
            return False

    def fillWithEmptyRooms(self):
        for x in range(self.numOfRows):
            for y in range(self.numOfColumns):
                self.placeRoom(Room(), Coordinates(x, y))
