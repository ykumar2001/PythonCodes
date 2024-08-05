# create a class 2-d vector and use it to create another class representing a 3-d vector.
class vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
        
    def add(self,other):
        return vector2D(self.x+other.x,self.y+other.y) 
    def subract(self,other):
        return vector2D(self.x-other.x,self.y-other.y) 
    def multiplication(self,scalar):
        return vector2D(self.x*scalar,self.y*scalar)

class vector3D(vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def add(self,other):
        return vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
    def substract(self,other):
        return vector3D(self.x-other.x,self.y-other.y,self.z-other.z)
    def multiplication(self,scalar):
        return vector3D(self.x*scalar,self.y*scalar,self.z*scalar)
# v2d1=vector2D(1,2)
# v2d2=vector2D(3,4)
# print(f"2D vector: {v2d1}")    
# print(f"2D vector: {v2d2}"),print("")
# print("addition:",v2d1.add(v2d2)),print("")
# print("subraction:",v2d1.subract(v2d2)),print("") 
# print("multiplication:",v2d1.multiplication(2)),print("")

v3d1=vector3D(1,2,3)
v3d2=vector3D(4,5,6)
print(f"3D vector: {v3d1}")    
print(f"3D vector: {v3d2}"),print("")
print("addition:",v3d1.add(v3d2)),print("")
print("subraction:",v3d1.subract(v3d2)),print("") 
print("multiplication:",v3d1.multiplication(2)),print("")
    
    