class employee :
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary 

    def showdetails(self):
        print("role: ",self.role)
        print("department: ",self.dept)
        print("salary: ",self.salary)
class engineer(employee) :
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("ENGINEER","IT",65000)
engg1=engineer("vikas",23)
engg1.showdetails()        

e1= employee("hr","acc",2000)
e1.showdetails()       