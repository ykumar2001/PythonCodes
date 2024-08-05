#single inheritance 
class car:
    colour="white"
    @staticmethod
    def start():
        print("car started.....")
    @staticmethod
    def stop():
        print("car stopped.....")
class toyotacar(car):
    def __init__(self,name):
        self.name=name

c1=toyotacar("fortuner")
c2=toyotacar("prius")
print(c1.name)        
print(c1.name,c1.start())
print(c1.colour)



#multi-level inheritance
class A:
    varA ="welocome to class A"
class B:
    varB ="welocome to class B"
class C(A,B):
    varC ="welcome to class c"

c1=C()
print(c1.varA)



#super  method 
class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped") 
class toyotacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
car1=toyotacar("prius","electric")
print(car1.type)                   

#classmethods


class person :
    name ="yogesh "
    def changename(self,name):
        self.name=name

p1=person()
p1.changename("raghav")
print(p1.name)
print(person.name)



class person :
    name ="yogesh "
    def changename(self,name):
        person.name=name

p1=person()
p1.changename("raghav")
print(p1.name)

# class method :

class person :
    name ="yogesh "
    #def changename(obj,name):
    # self.__class__.name="rahul"
    @classmethod
    def changename(cls,name):
        cls.name=name

p1=person()
p1.changename("rahul")
print(p1.name)
print(person.name)



# property 
class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.maths=maths
        self.chem=chem
        

    @property
    def percentage(self):
        return str((self.chem+self.phy+self.maths)/3)+"%"
std1=student(90,87,76)
print(std1.percentage)        

std1.phy=31
print(std1.percentage)