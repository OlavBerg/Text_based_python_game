# Developed by Olav Berg

from item import Item
from flashlight import Flashlight
from key import Key
from room_matrix import RoomMatrix
from coordinates import Coordinates
from inventory import Inventory

class Game:
    def __init__(self, roomMatrix: RoomMatrix):
        self.roomMatrix = roomMatrix
        self.currentCoordinates = Coordinates(0, 0)
        self.inventory = Inventory()
        self.isRunning = True

    def currentRoom(self):
        return self.roomMatrix.getRoom(self.currentCoordinates)

    def validDirection(self, direction: str):
        return direction in ["north", "east", "south", "west"]
    
    def move(self, subCommandList: list[str]):

        if len(subCommandList) < 2:
            print("Please type the direction you want to move.")
            return False

        direction = subCommandList[1] # The direction you want to move.

        if not self.validDirection(direction):
            print("Invalid direction.")
            return False

        direction = direction[0]
        door = self.currentRoom().getDoor(direction) # The door you want to move through.

        if door == None:
            print("There is no door in that direction.")
            return False
        elif door.isLocked():
            print("The door is locked.")
            return False

        nextCoordinates = self.currentCoordinates.getNext(direction)
        nextRoom = self.roomMatrix.getRoom(nextCoordinates)

        if nextRoom == None:
            print("There is a solid wall behind the door.")
            return False
        elif not nextRoom.containsLamp():
            flashlight = self.inventory.getFlashlight()

            if flashlight == None:
                print("The room has no lights. You need a flashlight to enter this room.")
                return False

        self.currentCoordinates = nextCoordinates
        print("You walk through the door.")
        return True

    def unlock(self, subCommandList: list[str]):

        if len(subCommandList) < 4:
            print("Please include the direction of the door you want to unlock and the color and shape of the key you want to use.")
            return False

        direction = subCommandList[1] # The direction of the door you want to unlock.

        if not self.validDirection(direction):
            print("Invalid direction.")
            return False

        keyColor = subCommandList[2]
        keyShape = subCommandList[3]
        key = self.inventory.getKey(keyColor, keyShape)

        if key == None:
            print("You don't have such a key.")
            return False

        direction = direction[0]
        door = self.currentRoom().getDoor(direction) # The door you want to unlock.

        if door == None:
            print("There is no door in that direction.")
            return False

        elif not door.isLocked():
            print("The door is already open.")
            return False

        elif not door.unlock(key):
            print("The key doesn't match.")
            return False

        print("You unlock the door.")
        self.inventory.remove(key)
        return True

    def getItemsOfType(self, itemType: type, itemList: list[Item]):
        """Given a list of items and an item type (key/flashlight), the function returns a list of all of the items of the given list that are the given type."""

        listOfItemsOfType = []

        for item in itemList:
            if isinstance(item, itemType):
                listOfItemsOfType.append(item)

        return listOfItemsOfType

    def pick(self, subCommands: list[str]):

        if len(subCommands) < 2:
            print("Please include the name of the item you want to pick up.")
            return False

        itemType = subCommands[-1]
        itemsOnFloor = self.currentRoom().getItemsOnFloor()

        pickedUpItem = None

        if itemType == "key":

            if len(subCommands) < 4:
                print("Please include the color and shape of the key you want to pick up.")
                return False

            color = subCommands[1]
            shape = subCommands[2]

            pickedUpKey = None

            for key in self.getItemsOfType(Key, itemsOnFloor):
                if key.getColor() == color and key.getShape() == shape:
                    pickedUpKey = key
                    break

            if pickedUpKey == None:
                print("There is no such key on the floor.")
                return False

            pickedUpItem = pickedUpKey
        
        elif itemType == "flashlight":
            try:
                pickedUpItem = self.getItemsOfType(Flashlight, itemsOnFloor)[0]
            except:
                print("There is no flashlight on the floor.")
                return False

        if pickedUpItem == None:
            print("There is no such item on the floor.")
            return False

        self.inventory.append(pickedUpItem)
        self.currentRoom().removeItem(pickedUpItem)

        subCommands.pop(0)
        itemName = " ".join(subCommands)

        print("You pick up the " + itemName + ".")
        return True

    def directionInfo(self, direction: str):
        """Returns a string describing what exists in the given direction (a wall, a door etc.)."""

        door = self.currentRoom().getDoor(direction)

        if door == None:
            return "Wall"
        elif door.isLocked():
            color = door.getColor()
            shape = door.getShape()

            return "Locked door (" + color.capitalize() + " " + shape.lower() + ")"
        else:
            return "Open door"

    def printItemList(self, itemList: list[Item]):
        for item in itemList:
            if isinstance(item, Key):
                key = item
                color = key.getColor()
                shape = key.getShape()
                print("• " + color.capitalize() + " " + shape.lower() + " key")

            elif isinstance(item, Flashlight):
                print("• Flashlight")

    def printGameState(self):
        """Prints the state if the game. Includes the current room, the doors in the room and the items on the floor."""
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Current room: " + self.currentCoordinates.toString())

        print("")

        print("North: " + self.directionInfo("n"))
        print("East:  " + self.directionInfo("e"))
        print("South: " + self.directionInfo("s"))
        print("West:  " + self.directionInfo("w"))

        print("")

        print("Items on the floor")
        print("------------------")
        self.printItemList(self.currentRoom().getItemsOnFloor())

        print("")

        print("Inventory")
        print("---------")
        self.printItemList(self.inventory.getItems())

    def showCommands(self):
        print("")
        print("Commands")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("• move {north/east/south/west}                                        Move in the given direction.")
        print("• pick {item name}                                                    Pick up the item with the given name.")
        print("• unlock {north/east/south/west} {key color} {key shape}              Unlock the door in the given direction using the key with the given color and shape.")
        print("• quit                                                                Quit the game.")
        print("• c                                                                   Show possible commands.")
        print("")

    def checkForRiddle(self):
        """Checks if there is a riddle in the current room. If there is, the riddle activates."""

        riddle = self.currentRoom().getRiddle()
            
        if riddle != None:
            riddleSolved = riddle.activate()

            if riddleSolved:
                self.currentRoom().removeRiddle()
            else:
                self.currentCoordinates = Coordinates(0, 0) # Teleport back to the start if you give an incorrect answer enough times.

    def start(self):
        print("Welcome to the game!")
        self.isRunning = True
    
    def quit(self):
        print("Quitting the game.")
        self.isRunning = False

    def enterCommand(self):
        """Asks the player to input a command, then executes it."""

        print("Type 'c' to show possible commands.")
        print("")

        while True:
            command = input("Command: ").lower()
            subCommandList = command.split(" ")

            successfulCommand = False

            if subCommandList[0] == "move":
                successfulCommand = self.move(subCommandList)
            elif subCommandList[0] == "pick":
                successfulCommand = self.pick(subCommandList)
            elif subCommandList[0] == "unlock":
                successfulCommand = self.unlock(subCommandList)
            elif subCommandList[0] == "quit":
                self.quit()
                break
            elif subCommandList[0] == "c":
                self.showCommands()
                continue
            else:
                print("Invalid command. Please type 'c' for a list of possible commands.")
                continue

            if successfulCommand:
                break

    def run(self):
        """Runs the game."""

        self.start()

        while self.isRunning:
            print("")

            if self.currentRoom().isFinish():
                print("Congratulations! You reached the finish room!")
                self.isRunning = False
                break

            self.checkForRiddle()

            self.printGameState()
            print("")
            self.enterCommand()