import collections
from door import Door
from collections import deque
from riddle import Riddle
from lamp import Lamp
from button import Button
from item import Item
from key import Key
from flashlight import Flashlight


class Room:
    def __init__(self, listOfDoor: list[Door] = None, itemsOnFloor: list[Item] = None, riddle: Riddle = None, lamp: Lamp = None, button: Button = None):
        if listOfDoor == None:
            self.listOfDoor = [None, None, None, None]
        else:
            self.listOfDoor = listOfDoor

        if itemsOnFloor == None:
            self.itemsOnFloor = []
        else:
            self.itemsOnFloor = itemsOnFloor

        self.finish = False #True if the room is the finish room. False otherwise.

        self.riddle = riddle

        self.lamp = lamp
        
        self.button = button

        


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
        

    def removeItem(self, item: Item):
      self.itemsOnFloor.remove(item)
      return self.itemsOnFloor

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

    def getItemsOnFloor(self):
        return self.itemsOnFloor

    def placeItemOnFloor(self, item: Item) :
        self.itemsOnFloor.append(item)

    """ def rotateRoom(self, direction: str):
        Rotates the room in the given direction. 'direction' is either 'c' (clockwise) or 'a' (anticlockwise).
        self.direction = collections.deque(self.listOfDoor)
        print("list before rotate")
        self.getDoor.rotate(self.listOfDoor)
        print("list after rotate")
        return self.getDoor() """
    

    def isFinish(self):
        return self.finish

    def setToFinish(self):
        """Returns True if the room is a finish room. Returns False otherwise."""
        self.finish = True

    def isEmpty(self):
        """Returns True if the room contains no doors and no items. Returns False otherwise."""
        if self.listOfDoor == None and self.itemsOnFloor == None and self.finish == False:
            return True

    def getRiddle(self) :
        return self.riddle

    def setRiddle(self, riddle: Riddle) :
        self.riddle = riddle
        
    def removeRiddle(self) :
        self.riddle = None
        
    def getLamp(self):
        return self.lamp

    def getButton(self):
        return self.button

    def setLamp(self, lamp: Lamp):
        self.lamp = lamp

    def setButton(self, button: Button):
        self.button = button 

    def containsLamp(self):
        if self.lamp != None:
            return True
        else:
            return False
    


  



        

        

        
           

    
            


        

        


        




        

        
            
            


    




        
        

        



            


