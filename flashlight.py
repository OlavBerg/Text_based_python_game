from item import Item

class Flashlight(Item) :
    def __init__(self, turnOn: False):
        super().__init__()
        self.turnOn = turnOn

    def turnOnFlashLight(self):
        if self.turnOn == False:
            self.turnOn = True
        print("Light is flashing!")
    
    def turnOffFlashlight(self):
        if self.turnOn == True:
            self.turnOn = False
        print("Flashlight is turned off!")

       
    
    
