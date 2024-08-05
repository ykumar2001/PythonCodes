# addition 
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
    
    def add (self,num2):
        newreal = self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)

num1=complex(1,3)            
num1.shownumber()

num2=complex(4,6)            
num2.shownumber()
num3=num1.add(num2)
num3.shownumber()



# substraction 


class complex:
    def __init__(self,real,img):
     self.real=real
     self.img=img 

    def shownum(self):
     print(self.real,"i +",self.img,"j")
      
    def __sub__(self,num2):
      newreal=self.real-num2.real
      newimg=self.img-num2.img
      return complex(newreal,newimg)

num1=complex(4,8)
num1.shownum()

num2=complex(6,9)
num2.shownum()  

num3=num1-num2
num3.shownum()
