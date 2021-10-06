from game import Game
from room_matrix import RoomMatrix
from coordinates import Coordinates
from room import Room
from riddle import Riddle
from door import Door
from key import Key
from lamp import Lamp
from flashlight import Flashlight

print("")

numOfRows = 2
numOfColumns = 3

roomMatrix = RoomMatrix(numOfRows, numOfColumns)
roomMatrix.fillWithEmptyRooms()

for x in range(numOfRows):
    for y in range(numOfColumns):
        roomMatrix.getRoom(Coordinates(x, y)).setLamp(Lamp(False))

key = Key("red", "square")
flashlight = Flashlight(True)

roomMatrix.getRoom(Coordinates(0, 0)).placeItemOnFloor(key)
roomMatrix.getRoom(Coordinates(0, 0)).placeItemOnFloor(flashlight)

lockedDoor1 = Door(True, "red", "square")
lockedDoor2 = Door(True, "green", "triangle")

roomMatrix.getRoom(Coordinates(0, 1)).setDoor("e", lockedDoor1)
roomMatrix.getRoom(Coordinates(0, 0)).setDoor("s", lockedDoor2)

roomMatrix.getRoom(Coordinates(0, 0)).setDoor("e", Door(False))
roomMatrix.getRoom(Coordinates(0, 1)).setDoor("w", Door(False))
roomMatrix.getRoom(Coordinates(0, 1)).setDoor("s", Door(False))
roomMatrix.getRoom(Coordinates(0, 2)).setDoor("w", Door(False))
roomMatrix.getRoom(Coordinates(1, 0)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(1, 1)).setDoor("n", Door(False))

riddle = Riddle("What is the name of greatest videogame\n"
            "ever created\n"
            "is it, Skyrim, Assassins Creed or World of Warcraft.", correctAnswer = 'skyrim', timesToTry = 3)

roomMatrix.getRoom(Coordinates(0, 1)).setRiddle(riddle)

roomMatrix.getRoom(Coordinates(1, 1)).lamp = None

roomMatrix.getRoom(Coordinates(0, 2)).setToFinnish()

game = Game(roomMatrix)
game.run()

print("")