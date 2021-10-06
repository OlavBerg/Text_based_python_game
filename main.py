from coordinates import Coordinates
from flashlight import Flashlight
from game import Game
from room_matrix import RoomMatrix
from key import Key
from door import Door
from riddle import Riddle
from lamp import Lamp

print("")

roomMatrix = RoomMatrix(5, 5)
roomMatrix.fillWithEmptyRooms()

finnishRoom = roomMatrix.getRoom(Coordinates(1, 3))
finnishRoom.setToFinnish()

# Keys and locked doors
key1 = Key("red", "circle")
lockedDoor1 = Door(True, "red", "circle")

key2 = Key("green", "square")
lockedDoor2 = Door(True, "green", "square")

key3 = Key("black", "pentagon")
lockedDoor3 = Door(True, "black", "pentagon")

key4 = Key("orange", "star")
lockedDoor4 = Door(True, "orange", "star")

key5 = Key("purple", "triangle")
lockedDoor5 = Door(True, "purple", "triangle")

key6 = Key("yellow", "rectangle")
lockedDoor6 = Door(True, "yellow", "rectangle")

key7 = Key("pink", "square")
lockedDoor7 = Door(True, "pink", "square")

key8 = Key("white", "oval")
lockedDoor8 = Door(True, "white", "oval")





# Place keys
roomMatrix.getRoom(Coordinates(1, 4)).placeItemOnFloor(key1)
roomMatrix.getRoom(Coordinates(3, 3)).placeItemOnFloor(key2)
roomMatrix.getRoom(Coordinates(3, 0)).placeItemOnFloor(key3)
roomMatrix.getRoom(Coordinates(4, 4)).placeItemOnFloor(key4)
roomMatrix.getRoom(Coordinates(2, 0)).placeItemOnFloor(key5)
roomMatrix.getRoom(Coordinates(3, 2)).placeItemOnFloor(key6)
roomMatrix.getRoom(Coordinates(4, 3)).placeItemOnFloor(key7)
roomMatrix.getRoom(Coordinates(1, 0)).placeItemOnFloor(key8)



# Place locked doors
roomMatrix.getRoom(Coordinates(1, 2)).setDoor("s", lockedDoor1)
roomMatrix.getRoom(Coordinates(2, 2)).setDoor("w", lockedDoor2)
roomMatrix.getRoom(Coordinates(3, 4)).setDoor("s", lockedDoor3)
roomMatrix.getRoom(Coordinates(2, 1)).setDoor("w", lockedDoor4)
roomMatrix.getRoom(Coordinates(3, 1)).setDoor("e", lockedDoor5)
roomMatrix.getRoom(Coordinates(4, 1)).setDoor("e", lockedDoor6)
roomMatrix.getRoom(Coordinates(0, 0)).setDoor("s", lockedDoor7)
roomMatrix.getRoom(Coordinates(0, 3)).setDoor("s", lockedDoor8)



# Place open doors
roomMatrix.getRoom(Coordinates(0, 0)).setDoor("e", Door(False))

roomMatrix.getRoom(Coordinates(0, 1)).setDoor("s", Door(False))
roomMatrix.getRoom(Coordinates(0, 1)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(0, 2)).setDoor("e", Door(False))
roomMatrix.getRoom(Coordinates(0, 2)).setDoor("s", Door(False))

roomMatrix.getRoom(Coordinates(0, 3)).setDoor("e", Door(False))
roomMatrix.getRoom(Coordinates(0, 3)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(0, 4)).setDoor("s", Door(False))
roomMatrix.getRoom(Coordinates(0, 4)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(1, 0)).setDoor("n", Door(False))

roomMatrix.getRoom(Coordinates(1, 1)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(1, 1)).setDoor("e", Door(False))

roomMatrix.getRoom(Coordinates(1, 2)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(1, 2)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(1, 3)).setDoor("n", Door(False))

roomMatrix.getRoom(Coordinates(1, 4)).setDoor("n", Door(False))

roomMatrix.getRoom(Coordinates(2, 0)).setDoor("e", Door(False))

roomMatrix.getRoom(Coordinates(2, 1)).setDoor("e", Door(False))
roomMatrix.getRoom(Coordinates(2, 1)).setDoor("s", Door(False))

roomMatrix.getRoom(Coordinates(2, 2)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(2, 2)).setDoor("e", Door(False))

roomMatrix.getRoom(Coordinates(2, 3)).setDoor("e", Door(False))
roomMatrix.getRoom(Coordinates(2, 3)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(2, 4)).setDoor("s", Door(False))
roomMatrix.getRoom(Coordinates(2, 4)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(3, 0)).setDoor("s", Door(False))

roomMatrix.getRoom(Coordinates(3, 1)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(3, 1)).setDoor("s", Door(False))

roomMatrix.getRoom(Coordinates(3, 2)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(3, 3)).setDoor("e", Door(False))

roomMatrix.getRoom(Coordinates(3, 4)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(3, 4)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(4, 0)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(4, 0)).setDoor("e", Door(False))

roomMatrix.getRoom(Coordinates(4, 1)).setDoor("n", Door(False))
roomMatrix.getRoom(Coordinates(4, 1)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(4, 2)).setDoor("e", Door(False))
roomMatrix.getRoom(Coordinates(4, 2)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(4, 3)).setDoor("w", Door(False))

roomMatrix.getRoom(Coordinates(4, 4)).setDoor("n", Door(False))



# Place riddles
r1 = Riddle("What is the name of greatest videogame\n"
            "ever created\n"
            "is it, Skyrim, Assassins Creed or World of Warcraft.", correctAnswer = 'skyrim', timesToTry = 3)

r2 = Riddle("There was a famous viking king who lived during the 9th century.\n"
            "His lastname is used as the name for a wireless connection technique (Bluetooth).\n"
            "But what was his firstname.\n"
            "Was it Harald, Ragnar or Olof\n", correctAnswer = 'harald', timesToTry = 2)

r3 = Riddle("A man who was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?\n"
            "'He was running', 'he was bald' or 'he was already wet'\n", correctAnswer =  'he was bald', timesToTry = 2)

r4 = Riddle("The more of this there is, the less you see. What is it?\n"
            "Is it, 'Trees' or 'Darkness'?\n", correctAnswer = 'darkness', timesToTry = 1)

r5 = Riddle("What is always infront of you but can't be seen?\n"
            "the future, a fast animal or the sun: \n", correctAnswer = 'the future', timesToTry = 2)

r6 = Riddle("I have keys but no locks, and space and no rooms\n"
            "you can enter but you can't go outside, what am i?"
            "This riddle has a one word answer", correctAnswer = 'keyboard', timesToTry = 30)

roomMatrix.getRoom(Coordinates(0, 2)).setRiddle(r1)
roomMatrix.getRoom(Coordinates(2, 3)).setRiddle(r2)
roomMatrix.getRoom(Coordinates(4, 0)).setRiddle(r3)
roomMatrix.getRoom(Coordinates(4, 4)).setRiddle(r4)
roomMatrix.getRoom(Coordinates(2, 0)).setRiddle(r5)
roomMatrix.getRoom(Coordinates(1, 0)).setRiddle(r6)



# Flashlight
flashlight = Flashlight(True)
roomMatrix.getRoom(Coordinates(3, 1)).placeItemOnFloor(flashlight)


# Place a lamp in every room
for x in range(5):
    for y in range(5):
        roomMatrix.getRoom(Coordinates(x, y)).setLamp(Lamp(False))


# Remove the lamp in certain rooms
roomMatrix.getRoom(Coordinates(2, 0)).lamp = None
roomMatrix.getRoom(Coordinates(4, 1)).lamp = None
roomMatrix.getRoom(Coordinates(1, 0)).lamp = None

# Set finnish room
roomMatrix.getRoom(Coordinates(1, 3)).setToFinnish()




game = Game(roomMatrix)
game.run()

print("")