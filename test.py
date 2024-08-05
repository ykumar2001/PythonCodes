#######BSC students details ######
class students_details:
    def __init__(self,name,age,mobno):
      
        self.name=name 
        self.age=age
        self.mobno=mobno
    def details(self):
        print("hello my name is",self.name,",my age is",self.age,"and my mobno is",self.mobno)     
        
s1=students_details("vikas",22,88484984)      
s2=students_details("nav",23,324641444)
s3=students_details("deep",22,4684687447)
s1.details()
s2.details()
s3.details()