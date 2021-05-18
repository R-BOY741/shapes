class Shapes :
def __init__(self, side, type, size, name):
        self.side=side
        self.type=type
        self.name=name

    def area(self):
        print("i am a" + self.name + "\n"
              "i have" + self.side + "\n"
              "I am a" + self.type + "\n"
              "i have" + self.size)
obj_shape=Shapes("shape", "4", "polygon", "14cm")
obj_shape.area()
class Circle(Shapes):

def __init__(self, radius):
     self.radius=radius
     def area(self):
         results= 3.14*self.radius* self.radius
         print( results)
obj_coin=Circle(5)
obj_coin.area()
class Triangle(Shapes):
    def __init__(self, base, height):
    self.base=base
    self.height=height




