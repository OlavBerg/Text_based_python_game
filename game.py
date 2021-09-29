from key import Key
from room_matrix import RoomMatrix

class Game:
    def init(self, roomMatrix: RoomMatrix):
        self.roomMatrix = roomMatrix
        self.currentRoom = roomMatrix.getRoom(0, 0)
        self.keysInInventory = []

    def move(self, direction: str):
        """If possible, moves the player to the next room in the given direction, which is either 'n', 'e', 's' or 'w'."""

        door = self.currentRoom.getDoor(direction)

        if door == None:
            print("There is no door in that direction.")
            return False
        elif door.isLocked():
            print("The door is locked.")
            return False
        else:
            currentCoordinates = self.currentRoom.getCoordinates()
            currentXCoordinate = currentCoordinates[0]
            currentYCoordinate = currentCoordinates[1]

            nextCoordinates = None
            if direction == "n":
                nextCoordinates = [currentXCoordinate - 1, currentYCoordinate]
            elif direction == "e":
                nextCoordinates = [currentXCoordinate, currentYCoordinate + 1]
            elif direction == "s":
                nextCoordinates = [currentXCoordinate + 1, currentYCoordinate]
            elif direction == "w":
                nextCoordinates = [currentXCoordinate, currentYCoordinate - 1]
            else:
                print("Error: Invalid direction.")

            nextRoom = self.roomMatrix.getRoom(nextCoordinates)
            self.currentRoom = nextRoom

            print("You walk through the door.")
            return True

    def unlock(self, direction: str, key: Key):
        door = self.currentRoom.getDoor(direction)

        if door == None:
            print("There is no door in that direction.")
        elif not door.isLocked():
            print("The door is already open.")
        elif door.unlock(key):
            print("You unlock the door.")
        else:
            print("The key doesn't match.")

    def pickKey(self, color: str, shape: str):
        pickedUpKey = None

        for key in self.currentRoom.getKeysOnFloor():
            if key.getColor() == color & key.getShape() == shape:
                pickedUpKey = key
                break

        if pickedUpKey == None:
            print("There is no such key on the floor.")
            return False
        else:
            self.keysInInventory.append(pickedUpKey)
            self.currentRoom.removeKey(key)
            print("You pick up the " + color + " " + shape + " key.")
            return True

    def directionInfo(self, direction: str):
        door = self.currentRoom.getDoor(direction)

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

        currentCoordinates = self.currentRoom.getCoordinates()
        currentXCoordinate = currentCoordinates[0]
        currentYCoordinate = currentCoordinates[1]
        print("Current room: (" + str(currentXCoordinate) + ", " + str(currentYCoordinate) + ")")

        print("")

        print("North: " + self.directionInfo("n"))
        print("East:  " + self.directionInfo("e"))
        print("South: " + self.directionInfo("s"))
        print("West:  " + self.directionInfo("w"))

        print("")

        print("Keys on floor")
        print("-------------")

        for key in self.currentRoom.getKeysOnFloor():
            color = key.getColor()
            shape = key.getShape()
            
            print("• " + color.capitalize() + " " + shape.lower())

        print("")

        print("Keys in inventory")
        print("-----------------")

        for key in self.keysInInventory:
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


    def getKeyFromInventory(self, color: str, shape: str):
        selectedKey = None

        for key in self.keysInInventory:
            if key.getColor() == color & key.getShape() == shape:
                selectedKey = key
                break
        
        return selectedKey

    def run(self):
        """Runs the game."""

        isRunning = True

        while isRunning:
            print("")

            trap = self.currentRoom().getTrap()

            if trap != None: 
                trap.activate()

            self.printGameState()
            print("")
            print("Type 'c' to show possible commands.")
            print("")

            while True:
                playerCommand = input("Command: ").lower()
                subCommands = playerCommand.split(" ")

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
                    self.isRunning = False
                    print("Quitting the game.")
                    break

                elif subCommands[0] == "c":
                    self.showCommands()
                    continue

                else:
                    print("Invalid command.")
                    continue
