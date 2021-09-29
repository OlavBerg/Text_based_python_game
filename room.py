from door import Door
from key import Key
import definedKeys
import definedDoors
 


class Room:
    def __init__(self, coordinates: list[int]):
        
        self.coordinates = coordinates
        self.listOfDoors = [None, None, None, None]
        self.keysOnFloor = []

    def setDoor(self, direction: str, door: Door):
        """Places a door in the given direction, which is either 'n', 'e', 's' or 'w'."""
        self.listOfDoors[]

        if direction == "North" :
            return definedDoors.redSquareDoor
        
        elif direction == "East" :
            return definedDoors.blackRoundDoor
        
        elif direction == "South" :
            return definedDoors.yellowTriangleDoor
        
        elif direction == "West" :
            return definedDoors.blueStarDoor
        

    def removeKey(self, key: Key):
        """Removes the given key from the KeysOnFloor list."""

        if key.color and key.shape == self.keysOnFloor :

            self.keysOnFloor.remove()


            
    def getDoor(self, direction: str):
        return direction

    def getCoordinates(self):
        return self.coordinates

    def getDoor(self, direction: str):
        """Returns the door in the given direction, which is either 'n', 'e', 's' or 'w'."""
        return direction(definedDoors)
        
    def getKeysOnFloor(self):
        return self.keysOnFloor

    

    

        

        

        

        


        
        

         




        

    
        

        


        

            
        
        










        

