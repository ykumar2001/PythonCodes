#program to generate aadharcard password using name and dob

name=input("enter your name: ")
dob=input("enter your dob in 'dd/mm/yyyy': ")

result=name[0:4]+dob[-4:]
print(f'your new aadharcard password is:{result} ')