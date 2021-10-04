from door import Door
from key import Key

class Room:
    def __init__(self, coordinates: list[int]):
        self.coordinates = coordinates
        self.listOfDoor = [None, None, None, None]
        self.keysOnFloor = []


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


        
            


        

        


        




        

        
            
            


    




        
        

        



            


