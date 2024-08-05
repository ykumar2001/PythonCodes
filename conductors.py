#create acccount class with 2 attributees-balance & account no. 
#create methods for debit,credit & printing the balance.

class account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"is debited from your account")
        print("total balance=",self.get_balance())

    #credit method 
    def credit(self,amount):
        self.balance +=  amount 
        print("Rs.",amount,"is credited from your account")  
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
p1=account(2000,1234)

print(p1.balance,p1.account_no)
p1.debit(1000)
p1.credit(500)




