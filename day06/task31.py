import math
class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length 
        self.breadth=breadth 
    def area(self):
        return self.length*self.breadth  
class triangle(shape):
    def __init__(self,base,height):
        self.base=base 
        self.height=height 
    def area(self):
        return 0.5*self.base*self.height    
c = circle(5)
r = rectangle(4, 6)
t = triangle(5,7)
print(c.area())   
print(r.area())      
print(t.area())        

               