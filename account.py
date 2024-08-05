class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass)

p1=account(1234,"abcd") 
print(p1.acc_no)
# print(p1.__acc_pass)       
print(p1.reset_pass())