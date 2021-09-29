from door import Door

def printDoorState(door: Door) :
    if door.isClosed() :
        print("Door is closed!")
    else :
        print("Door is open!")

