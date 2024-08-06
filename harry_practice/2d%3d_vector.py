#create a class 2-d vector and use it to create another class representing a 3-d vector.

class vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"

    def add(self,other):
        return vector2d(self.x+other.x,self.y+other.y)
    def substract(self,other):
        return vector2d(self.x-other.x,self.y-other.y)
    def scalar_product(self,scalar):
        return vector2d(self.x*scalar,self.y*scalar)
class vector3d(vector2d):
    def __init__(self,x,y,z):
         super().__init__(x,y) 
         self.z=z    

    def __str__(self):
          return f"({self.x},{self.y},{self.z})"
    def add(self,other):
            return vector3d(self.x+other.x,self.y+other.y,self.z+other.z)
    def substract(self,other):
            return vector3d(self.x-other.x,self.y-other.y,self.z-other.z)
    def scalar_product(self,scalar):
        return vector3d(self.x*scalar,self.y*scalar,self.z*scalar)
v2d1=vector2d(1,2)
v2d2=vector2d(3,4)
print(f"2D vector:{v2d1}")    
print(f"2D vector:{v2d2}"),print()
print(f"addition:{v2d1.add(v2d2)}")
print(f"subsraction:{v2d1.substract(v2d2)}")
print(f"scalar product:{v2d1.scalar_product(2)}"),print()

v3d1=vector3d(9,8,7)
v3d2=vector3d(6,5,4)
print(f"3D vector:{v3d1}")
print(f"3D vector:{v3d2}"),print()
print(f"addition:{v3d1.add(v3d2)}")
print(f"subsraction:{v3d1.substract(v3d2)}")
print(f"scalar product:{v3d1.scalar_product(2)}"),print()