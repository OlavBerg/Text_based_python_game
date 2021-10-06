from item import Item

class Flashlight(Item) :
    def __init__(self, turnOn: bool = False):
        super().__init__()
        self.turnOn = turnOn

    def turnOnFlashLight(self):
        if self.turnOn == False:
            self.turnOn = True

    def turnOffFlashlight(self):
        if self.turnOn == True:
            self.turnOn = False

    def getTurnOn(self):
        return self.turnOn
    
    
   
        
    

    
   
        
    
    

       
    
    
