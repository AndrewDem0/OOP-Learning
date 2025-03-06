class Animal:
    def __init__(self, name, speed):
        self._name = name
        self._speed = speed
    
    def __del__(self):
        print("An inst of class Animal,"+self._name+" has been deleted")
    
    def sayHello(self):
        print("Hello, I am "+self._name+"  my speed is "+str(self._speed))
    
    def speedUp(self, delta):
        self._speed +=self._speed + delta
        
    def speedDown(self, delta):
        if(self._speed >= delta):
            self._speed = self._speed - delta
        else:
            self._stop()
            
    def _stop(self):    
        self._speed = 0
    
    def getName(self):
        return self._name
    
class Rabbit(Animal):
    def __init__(self, name, speed, jumpPerStep):
        Animal.__init__(self, name, speed)
        self._jumpPerStep = jumpPerStep
        self._jumpCounter = 0
    
    def __del__(self):
        print("An inst of class Rabbit,"+self._name+" has been deleted")
        print("The rabbit" +self._name+ "has jumped "+str(self._jumpCounter)+" times")
        
    def step(self, stepAmount):
        print("The rabbit "+self._name+" jumped "+str(self._jumpPerStep*stepAmount)+" times")
        self._jumpCounter += self._jumpCounter + self._jumpPerStep*stepAmount
        
        
an1 = Rabbit("Rabbit1", 10, 2)
an2 = Rabbit("Rabbit2", 20, 3)

an1.sayHello()

an2.sayHello()

del an1 
del an2