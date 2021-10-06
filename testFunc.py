from door import Door
from room import Room
from key import Key

def printDoorState(door: Door) :
    if door.isLocked() :
        print("Door is closed!")
    else :
        print("Door is open!")

def printKeyList(room: Room) :
    print("The inventory: ", room.keysOnFloor)
