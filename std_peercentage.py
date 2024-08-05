class students :
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        self.percentage=str((self.phy+self.chem+self.maths)/3) +"%"
    def calpercentage(self):
        self.percentage=str((self.phy+self.chem+self.maths)/3) +"%"

std1= students(98,87,91)
print(std1.percentage)
std1.phy =56
std1.calpercentage()

print(std1.calpercentage)
print(std1.percentage)





# property method

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