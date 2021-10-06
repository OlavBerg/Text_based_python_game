# Developed by Olav Berg

from room import Room
#from door import Door
from coordinates import Coordinates
#from key import Key
#import help_functions
#import random

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
    """
    def makePath(self, currentCoordinates: Coordinates, currentPath: list[Coordinates], lockedDoorList: list[Door]):

        if not(self.validCoordinates(currentCoordinates)) or currentCoordinates.inList(currentPath):
            return False
        
        currentPath.append(currentCoordinates)
        currentRoom = self.getRoom(currentCoordinates)

        if not(currentRoom.isEmpty()) or currentCoordinates.isEqual(Coordinates(0, 0)):
            return True

        uncheckedDirections = ["n", "e", "s", "w"]

        while len(uncheckedDirections) > 0:
            directionToNextRoom = random.choice(uncheckedDirections)
            nextCoordinates = currentCoordinates.getNext(directionToNextRoom)

            if self.makePath(nextCoordinates, currentPath, lockedDoorList):
                currentRoom.setDoor(directionToNextRoom, Door(False))

                nextRoom = self.getRoom(nextCoordinates)
                doorInNextRoom = None

                if nextRoom.isEmpty():
                    doorInNextRoom = Door(False)
                else: 
                    doorInNextRoom = Door(True)
                    lockedDoorList.append(doorInNextRoom)

                nextRoom.setDoor(help_functions.reverseDirection(directionToNextRoom), doorInNextRoom)
                return True
            else:
                uncheckedDirections.remove(directionToNextRoom)
    
        currentPath.pop(-1)
        return False


    def randomize(self, colorPool: list[str], shapePool: list[str]):

        self.fillWithEmptyRooms()
        emptyCoordinatesList = help_functions.doubleRange(self.numOfRows, self.numOfColumns)
        milestoneCoordinatesList = []
        lockedDoorList = []

        while len(emptyCoordinatesList) > 0:
            milestoneCoordinates = random.choice(emptyCoordinatesList)
            milestoneCoordinatesList.append(milestoneCoordinates)

            currentPath = [milestoneCoordinates]
            self.makePath(milestoneCoordinates, currentPath, lockedDoorList)
            help_functions.listSubtraction(emptyCoordinatesList, currentPath)

        availableColorShapePairs = help_functions.listOfPairs(colorPool, shapePool)

        for i in range(len(lockedDoorList)):
            colorShapePair = random.choice(availableColorShapePairs)
            availableColorShapePairs.remove(colorShapePair)

            color = colorShapePair[0]
            shape = colorShapePair[1]

            roomWithKey = self.getRoom(milestoneCoordinatesList[i])
            roomWithKey.setKeyOnFloor(Key(color, shape))

            lockedDoor = lockedDoorList[i]
            lockedDoor.setColor(color)
            lockedDoor.setShape(shape)

        finnishRoom = milestoneCoordinatesList[-1]
        finnishRoom.setToFinnish()
    """

