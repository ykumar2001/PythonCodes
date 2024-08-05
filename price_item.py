class order :
    def __init__(self,items,price):
        self.price =price
        self.item=items
    def __gt__(self,odr2):
        return self.price > odr2.price

ord1= order("chips",20)
odr2= order("tea",10)
print(ord1>odr2)