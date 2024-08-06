# create a class employee and add salary and increment properties to it. 
# write a method salary after increment method with a @property decorator with a settere,
#  which change which changes the value of increment based on the salary.

class employee :
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
        