#program to generate a login id using name,dob,phone no.

a=input('enter your name: ')
b=input('enter your dob: ')
c=input('enter your phone no: ')

result=(a[0:6].upper()+b+c)
print(f'your login id is: {result}')
 