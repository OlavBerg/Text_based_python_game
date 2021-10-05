from key import Key
from door import Door
from button import Button
from lamp import Lamp
from room import Room
import testFunc
from flashlight import Flashlight

myRoom = Room([0,0], None, None, None, None)
myDoor = Door(True, "red", "circle")
myKey = Key("red", "circle")
myOtherKey = Key("blue", "square")
myLamp = Lamp(True)
myButton = Button(False)
myFlashlight = Flashlight(False)



 
# Test 1: See if room exist 
print("What do you see ahead?")
myRoom.setDoor("n", myDoor)
print("Empty room with a red circle door") 

# Test 0: Turn on the lights in the room/ Turn off the lights
print("The room is dark...")
myRoom.setLamp(myLamp)
myRoom.setLamp(myLamp.lightsOn(myButton))
print("Can you turn off the lights?")
myRoom.setLamp(myLamp.lightsOff(myButton))

# Test 2: See if key is on the floor
print("What is on the floor?")
myRoom.keysOnFloor.append(myKey)
testFunc.printKeyList(myRoom)
print("Red circle key")


# Test 3: Testing to open the door without the key
print("I want to open the door")
testFunc.printDoorState(myDoor)


# Test 4: Testing to open the door with the right key
print("Can i open the door with the red circle key")
myDoor.unlock(myKey)
testFunc.printDoorState(myDoor)

# Test 5: Testing to remove the keys from key list
print("Is the key removed?")
myRoom.removeKey(myKey)
testFunc.printKeyList(myRoom) 

# Test 6: Test the FlashLight

print("I can't see anything, it's so dark...")
print("I can use my flashlight...")
myFlashlight.turnOnFlashLight()
print("I want to turn off my flashlight...")
myFlashlight.turnOffFlashlight()
















