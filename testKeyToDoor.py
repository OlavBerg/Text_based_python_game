from door import Door
from key import Key
import testFunc



blackRoundKey = Key("Black", "Round")
blackRoundDoor = Door(True, "Black", "Round")

# Test 1: Test to see if door is initally closed
print("Expecting door to be closed")
testFunc.printDoorState(blackRoundDoor) 

# Test 2: Test to see if door opens with paired key that matches the color and shape
print("Expecting door to be open")
blackRoundDoor.unlock(blackRoundKey)
testFunc.printDoorState(blackRoundDoor)

redSquareKey = Key("Red", "Square")
blackRoundDoor = Door(True, "black", "round")

# Test 3: Test to see if door opens with wrong key to door 
print("Expecting door to be closed")
blackRoundDoor.unlock(redSquareKey)
testFunc.printDoorState(blackRoundDoor)


