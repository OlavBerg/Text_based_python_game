from button import Button

class Lamp :
    def __init__(self, initallyLightOff: True) :
        self.initiallyLightOff = initallyLightOff

    def lightsOn(self, button: Button) :
        if button.On :
            self.initiallyLightOff = False
            
    
    def lightsOff(self, button: Button) :
        if button.Off :
            self.initiallyLightOff 
            
    
    def getInitiallyLightOff(self) :
        return self.initiallyLightOff

    



        

    
        
        
    
    
    

 
    

    


        




  
        
