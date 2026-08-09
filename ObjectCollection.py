class Car :
    def __init__(self,speed,color) :
        self.speed = speed
        self.color = color
        
c1 = Car(240,"Red")
c2 = Car(300,"White")
c3 = Car(400,"Black")

li = [c1,c2,c3]

for c in li :
    print(c.speed,c.color)

#Here the objects are not stored inside the list . Actually the references to the objects are stored in the list.