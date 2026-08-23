#Method overriding

#If there is a method with same name always the child method is executed when its called.This is called method overriding.
#Same if there is a constructore in a child class then its executed this is called constructor overriding.

#super keyword

#The super() function in Python is a built-in function used to give a child class access to methods and properties
#of a parent class without naming the parent explicitly.

class Phone :
    def __init__(self,brand,price,cam) :
        print("Inside a mobile constructor")
        self.brand = brand
        self.price = price
        self.cam = cam

    def buy(self) :
        print("Buying a mobile")
    

class SmartPhone(Phone) :
    def __init__(self,brand,price,cam,ram,battery) :
        print("Inside smartphone constuctor")
        super().__init__(brand,price,cam)
        
        self.ram = ram
        self.battery = battery
        super().buy()

sp1 = SmartPhone("OPPO",23500,"50MP",8,7000)

#We dont need to pass self when used super keyword because when you use super(), Python automatically binds 
# and passes self behind the scenes. You do not pass it manually.

#Different ways

# Option A: Using super() -> Python injects 'self' automatically
super().__init__(brand, price, cam)

# Option B: Using Class Name -> You MUST pass 'self' manually
Phone.__init__(self, brand, price, cam)
