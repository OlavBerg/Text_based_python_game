from door import Door
from key import Key
from collections import deque
from riddle import Riddle

class Room:
    def __init__(self, listOfDoor: list[Door] = None, keysOnFloor: list[Key] = None, riddle: Riddle = None):
        if listOfDoor == None:
            self.listOfDoor = [None, None, None, None]
        else:
            self.listOfDoor = listOfDoor

        if keysOnFloor == None:
            self.keysOnFloor = []
        else:
            self.keysOnFloor = keysOnFloor

        self.finnish = False #True if the room is the finnish room. False otherwise.

        self.riddle = riddle

        


    def setDoor(self, direction: str, door: Door):
        """Places a door in the given direction, which is either 'n', 'e', 's' or 'w'."""
        
        
        if direction == "n" :
            self.listOfDoor[0] = door 
            
        
        elif direction == "e" :
            self.listOfDoor[1] = door
            

        elif direction == "s" :
            self.listOfDoor[2] = door 
        
        elif direction == "w" :
            self.listOfDoor[3] = door 
           
    def removeKey(self, key: Key):
      self.keysOnFloor.remove(key)
      return self.keysOnFloor

    def getDoor(self, direction: str):
        if direction == "n" :
            return self.listOfDoor[0]

        elif direction == "e" :
            return self.listOfDoor[1]

        elif direction == "s" :
            return self.listOfDoor[2]

        elif direction == "w" :
            return self.listOfDoor[3]


    def getCoordinates(self):
        return self.coordinates

    def getDirection(self, direction: str):
        """Returns the door in the given direction, which is either 'n', 'e', 's' or 'w'."""
        return direction 

    def getKeysOnFloor(self):
        return self.keysOnFloor

    def placeKeyOnFloor(self, key: Key) :
        self.keysOnFloor.append(key)

    def rotateRoom(self, direction: str):
        """Rotates the room in the given direction. 'direction' is either 'c' (clockwise) or 'a' (anticlockwise)."""
        self.getDoor = deque([0, 1, 2, 3])
        self.getDoor.rotate()
        print(self.getDoor)
        return self.listOfDoor


    def isFinnish(self):
        """Returns True if the room is a finnish room. Returns False otherwise."""
        self.finnish = True

    def isEmpty(self):
        """Returns True if the room contains no doors and no keys. Returns False otherwise."""
        if self.listOfDoor == None and self.keysOnFloor == None and self.finnish == False:
            return True

    def getRiddle(self) :
        return self.riddle

    def setRiddle(self, riddle: Riddle) :
        self.riddle = riddle


    
            


        

        


        




        

        
            
            


    




        
        

        



            


