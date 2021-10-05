from key import Key
from room_matrix import RoomMatrix
from coordinates import Coordinates

class Game:
    def __init__(self, roomMatrix: RoomMatrix):
        self.roomMatrix = roomMatrix
        self.currentCoordinates = Coordinates(0, 0)
        self.inventory = []

    def currentRoom(self):
        return self.roomMatrix.getRoom(self.currentCoordinates)

    def move(self, direction: str):
        """If possible, moves the player to the next room in the given direction, which is either 'n', 'e', 's' or 'w'."""

        door = self.currentRoom().getDoor(direction)

        if door == None:
            print("There is no door in that direction.")
            return False
        elif door.isLocked():
            print("The door is locked.")
            return False
        else:
            if direction == "n":
                self.currentCoordinates[0] -= 1
            elif direction == "e":
                self.currentCoordinates[1] += 1
            elif direction == "s":
                self.currentCoordinates[0] += 1
            elif direction == "w":
                self.currentCoordinates[1] -= 1
            else:
                print("Error: Invalid direction.")

            print("You walk through the door.")
            return True

    def unlock(self, direction: str, key: Key):
        door = self.currentRoom().getDoor(direction)

        if door == None:
            print("There is no door in that direction.")
            return False

        elif not door.isLocked():
            print("The door is already open.")
            return False

        elif door.unlock(key):
            print("You unlock the door.")
            self.keysInInventory.remove(key)
            return True

        else:
            print("The key doesn't match.")
            return False

    def pickKey(self, color: str, shape: str):
        pickedUpKey = None

        for key in self.currentRoom().getKeysOnFloor():
            if key.getColor() == color and key.getShape() == shape:
                pickedUpKey = key
                break

        if pickedUpKey == None:
            print("There is no such key on the floor.")
            return False
        else:
            self.inventory.append(pickedUpKey)
            self.currentRoom().removeKey(key)
            print("You pick up the " + color + " " + shape + " key.")
            return True

    def directionInfo(self, direction: str):
        door = self.currentRoom().getDoor(direction)

        if door == None:
            return "Wall"
        elif door.isLocked():
            color = door.getColor()
            shape = door.getShape()

            return "Locked door (" + color.capitalize() + " " + shape.lower() + ")"
        else:
            return "Open door"

    def printGameState(self):
        """Prints the state if the game. Includes the current room, the doors in the room and the keys on the floor."""
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")


        print("Current room: (" + str(self.currentCoordinates.getX()) + ", " + str(self.currentCoordinates.getY()) + ")")

        print("")

        print("North: " + self.directionInfo("n"))
        print("East:  " + self.directionInfo("e"))
        print("South: " + self.directionInfo("s"))
        print("West:  " + self.directionInfo("w"))

        print("")

        print("Keys on the floor")
        print("-----------------")

        for key in self.currentRoom().getKeysOnFloor():
            color = key.getColor()
            shape = key.getShape()
            
            print("• " + color.capitalize() + " " + shape.lower())

        print("")

        print("Keys in your inventory")
        print("----------------------")

        for key in self.inventory:
            color = key.getColor()
            shape = key.getShape()
            
            print("• " + color.capitalize() + " " + shape.lower())

    def showCommands(self):
        print("")
        print("Commands")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("• move {north/east/south/west}                                        Move in the given direction.")
        print("• pick {key color} {key shape}                                        Pick up the key with the given color and shape.")
        print("• unlock {north/east/south/west} {key color} {key shape}              Unlock the door in the given direction using the key with the given color and shape.")
        print("• quit                                                                Quit the game.")
        print("• c                                                                   Show possible commands.")
        print("")

    def getInventoryItemsOfType(self, itemType: type):
        itemList = []

        for item in self.inventory:
            if isinstance(item, itemType):
                itemList.append(item)

        return itemList

    def getKeyFromInventory(self, color: str, shape: str):
        selectedKey = None

        for key in self.getInventoryItemsOfType(Key):
            if key.getColor() == color & key.getShape() == shape:
                selectedKey = key
                break
        
        return selectedKey

    def run(self):
        """Runs the game."""

        isRunning = True
        print("Welcome to the game!")

        while isRunning:
            print("")

            riddle = self.currentRoom().getRiddle()
            
            if riddle != None:
                riddle.activate()

            self.printGameState()
            print("")
            print("Type 'c' to show possible commands.")
            print("")

            while True:
                playerCommand = input("Command: ").lower()
                subCommands = playerCommand.split(" ")

                try:
                    if subCommands[0] == "move":
                        direction = subCommands[1]

                        if not direction in ["north", "east", "south", "west"]:
                            print("Invalid direction.")
                            continue

                        direction = direction[0]

                        if self.move(direction):
                            break
                        else:
                            continue

                    elif subCommands[0] == "pick":
                        keyColor = subCommands[1]
                        keyShape = subCommands[2]

                        if self.pickKey(keyColor, keyShape):
                            break
                        else:
                            continue

                    elif subCommands[0] == "unlock":
                        direction = subCommands[1]
                        keyColor = subCommands[2]
                        keyShape = subCommands[3]
                        key = self.getKeyFromInventory(keyColor, keyShape)

                        if not direction in ["north", "east", "south", "west"]:
                            print("Invalid direction.")
                            continue

                        if key == None:
                            print("You don't have such a key.")
                            continue

                        direction = direction[0]

                        if self.unlock(direction, key):
                            break
                        else:
                            continue

                    elif subCommands[0] == "quit":
                        isRunning = False
                        print("Quitting the game.")
                        break

                    elif subCommands[0] == "c":
                        self.showCommands()
                        continue

                except:
                    print("Invalid command.")
                    continue
