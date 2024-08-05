class student():
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks
        
    def get_avg(self):
        sum=0
        print("marks before for loop",self.marks)

        for val in self.marks:
            sum += val
        print("hi",self.name ,"your avg score is :", sum/3)
    
s1= student("tony",[97,16,46])
s1.get_avg()
