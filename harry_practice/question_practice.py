# write a program to add two numbers

# print("enter your first nnumber : ")
# a=int(input())
# print("enter your second number : ")
# b=int(input())
# print("your required product is : "),print(a*b)

# write a program to find remainder when a number is divided by z
# print("enter your first number: ")
# num =int(input())
# print("enter your second number: ")
# z=int(input())
# print("your reminder is: ")
# print(num%z)


# check the type of the variable assigned using input() function

# a=input()
# print(type(a))


# use comparison operators to findout whether a given variable 'a' is greater than 'b' or not.Take a=34 and b=80.

# a=int(input())
# b=int(input())
# if a>b:
#   print("'a' is greater than 'b'",)

# write a python program to find the average of  two number entered by the user.

# print("enter your first number: ")
# a=int(input())
# print("enter your second number: ")
# b=int(input())
# print("your average is: ",(a+b)/2)


# write a program to caculate square of a number enter by the user.

# print("enter your number: ")
# a=int(input())
# print(a*a) 


# write a program to display a user entered name follwed by good afternoon using input() function.
# print("enter your username: ")
# a=str(input())
# print(a,",")
# print("Good Afternoon!")


# write a program to fill in a letter template given below with name and date.
#          letter =''' dear</name/>
#                      your selected !
#                            </date/> '''

# print("enter your name: ")
# name=input()
# print("enter date: ")
# date=input()
# letter=f'''dear {name}
#       you are selected!
#        {date} '''
# print("letter=",letter)

# write a program to delete double space in a string .

# a= "hello everyone! we are here to celebrate birthday "
# b="hey whatsup!"
# print(a.replace(" ",""))
# print(b.replace(" ",""))

# write a program to format the following letter using escape sequence characters.  letter ="dear Harry,this python cousre is nice.thanks! "

# letter="dearHarry,\nthis pyhton course is nice.\nthanks!"
# print(letter)

# write a program to store seven fruits in a list entered by the user.

# a = input("Name of 1st Fruit:  ")
# b = input("Name of 2nd Fruit:  ")
# c = input("Name of 3rd Fruit:  ")
# d = input("Name of 4th Fruit:  ")
# e = input("Name of 5th Fruit:  ")
# f = input("Name of 6th Fruit:  ")
# g = input("Name of 7th Fruit:  ")

# l = (a,b,c,d,e,f,g)
# print(l)

# write a program to accept marks of 6 studnets and display them in a sorted manner.

# a=input("enter marks of 1st student: ")
# b=input("enter marks of 2nd student: ")
# c=input("enter marks of 3rd student: ")
# d=input("enter marks of 4th student: ")
# e=input("enter marks of 5th student: ")
# f=input("enter marks of 6th student: ")

# l=[a,b,c,d,e,f]
# l.sort()
# print(l)

# check that a tuple cannot be changed in python.******************

# write a program to sum a list with 4 numbers.
# sum=0
# a=[1,2,3,4]
# for x in range(0,len(a)):
#     sum=sum + a[x]
# print(sum)

# write a program to count the number of zeros in the following tuple : a=(7,0,8,0,0,9)

# a=(7,0,8,0,0,9)
# b=a.count(0)
# print(b)


# ***************write a program to create a dictionary of hindi words with values as their english translation.Provide user with an option to look it up!

# from englisttohindi.englisttohindi import engtohindi
# txt="yes, i'm geeks"
# res =engtohindi(txt)
# print(res.convert)


# write a program to input eight numbers from the user and display all the unique number(once).
# l1=[]
# for x in range(9):
#     a=input("enter no.: ")
#     if a not in l1:
#      l1.append(a)
# print(l1)

# can we have a set with 18(int) and "18"(str) as a value in it? ******************************
# s1=set()
# s1.add(int(18))
# print(s1)
# s1.add(str(18))
# print(s1)

# what will be the length of following set s:
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")

# s=set()
# s.add(20)
# print(s)
# s.add(20.0)
# print(s)
# s.add("20")
# print(s)
# print(len(s))

# create an empty dictionary. allow 4 friends to enter their favourite language as values and use keys as their names. assume that the name are unique.

# friends={}
# friends.update({"f1":"english","f2":"hindi","f3":"german","f4":"france"})
# print(friends)

# can you change the value inside a lsit which is contained i set s. s={8,7,12,"harry",[1,2]} **********************


# write a program to find greatest of four numbers entered by the user.

# a=int(input("enter your 1st value: "))
# b=int(input("enter your 2nd value: "))
# c=int(input("enter your 3rd value: "))
# d=int(input("enter your 4th value: "))

# if a>b and b>c and c>d:
#     print(a,"is the greatest no.")
# if b>c and c>d:
#     print(b,"is the greatest mo.")
# if c>d:
#     print(c,"is the greatest no.")
# else:
#     print(d,"is the greatest no.")            

# write a program to find out whether a student is pass or fail,if it requires total 40% and atleat 33% in each subject to pass.
#  assume 3 subject and take marks as an input from the user.

# sub1=int(input())
# sub2=int(input())
# sub3=int(input())
# sum = (sub1+sub2+sub3)/3
# print(sum)
# if sub1>33 and sum>40:
#     print("you are pass") 
# elif sub2>33 and sum>40:
#     print("you are pass") 
# elif sub3>33 and sum>40:
#     print("you are pass") 
# else :
#     print("you are failed")    

# a spam comment is defined as a text containsing following keywords:
# "make a lot of money ","buy now ","subscribe this","click this ".write a program to delete these spams.

# comment=input("comment: ")
# if "make a lot of money" in comment:
#     print("spam!")
# elif "buy now" in comment:
#     print("spam!")
# elif    "subscribe this" in comment:
#     print("spam!")
# elif     "click this" in comment:
#     print("spam!")

# else: print(comment)

# write a program to find whether a given username contains less than 10 characters or not.

# usrname=input("username: ")
# if len(usrname)<10:
#     print("sorry!10 character required")
# else:
#     print(usrname)

# write a program which finds out whether a given name is present in a list or not.
# name=input("enetr your name : ")
# l1=['a','b','c','d']
# if name in l1:
#     print(name)
# else :
#     print("sorry!we lost")    

# write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 ->EX
# 80-90->A
# 70-80->B
# 60-70->C
# 50-60->F

# marks=int(input("enter your marks: "))
# if marks>90 and marks<=100:
#     print("excellent!")
# elif marks>80 and marks<90:
#     print("A")
# elif marks>70 and marks<80:
#     print("B")        
# elif marks>60 and marks<70:
#     print("C")
# elif marks>50 and marks<60:
#     print("F")
# else:pass

# write a program to find out whether a given post is talking about "harry" or not.


# pst=input("enter your post: ")
# if "harry" in pst:
#     print("hello! harry")
# else :
#     print("your are not the one,whome which we are looking for!")    

# write a program to print multiplication table of a given number using for loop.

# n=int(input())
# for x in range(0,10):
#     print(n,"x",x+1,"=",n*(x+1))

# write a program to greet all the person names sorted in a list l1 and which starts with s. l1=["harry","sohan","sachin","rahul"]

# l1=["harry","sohan","sachin","rahul"]
# for x in l1:
#  if(x.startswith('s')):
#     print(x)

# write a program to print multiplication table of a given number using while lopl.


# num=int(input("enter your number: "))
# i=0
# while i<10:
#     print(num,"x",i+1,"=",num*(i+1))
#     i+=1


# # write a program to find whether a given number is prime or not?

# n=int(input("enter you number: "))
# is_prime = True
# if n<=1:
#     is_prime=False
# else:
#     for i in range(2,n):
#         if n % i==0:
#             is_prime=False
#             break
# if is_prime:
#     print(f"{n}is a prime number")
# else:
#     print(f"{n}is not a prime number")                

## write a program to find the sum of first n natural number using while  loop.

# n=int(input("enter your number: "))
# sum_of_numbers=0
# current_number=1
# while current_number<=n:
#     sum_of_numbers+=current_number
#     current_number+=1
# print(f"the sum of first{n} natural is{sum_of_numbers}")

# write ta program to calculate the factorial of a given number using for loop.
# n=int(input("enter your number: "))
# factorial=1
# if n<0: print("factorial is not defined for negative ")
# else:
#     for i in range(1,n+1):
#         factorial*=i

#     for x in range(1,n+1):

#         print(f"the factorial of {n} is {factorial}")

# # write a program to print the following star pattern for n=3.
#     * 
#   * * *
# * * * * *

# n=3
# for x in range(n):
#    print(' '*(n-x-1),end=" ")
#    print("*"*(2*x+1))

##  write a program to print the following star pattern for n=3.
# *
# ** 
# ***

# n=3
# for x in range(n):
#     print(''*(n-x-1),end="")
#     print("*"*(x+1))


# Given a list, write a Python program to swap first and last element of the list.
# Examples: Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12] Input : [1, 2, 3] Output : [3, 2, 1]

# directly swaping elements of a list.
# l1=[12, 35, 9, 56, 24]
# l1[0],l1[-1]=l1[-1],l1[0]
# print(l1)


# # using a third variable to swap elements of a list.
# l2=[1, 2, 3] # second list given 
# i=0 # position of first element 
# j=-1 #postion of second element
# a=l2[i]
# l2[i]=l2[j]
# l2[j]=a
# print(l2)

# write a program to print thr following star pattern for n=3.
#  * * *
#  *   *
#  * * *

# n=3
# for x in range(n):
#   for y in range(n):
#     if x==0 or x==n-1 or y==0 or y==n-1:
#       print("*",end=" ")
#     else:
#       print(' ',end=" ")
#   print()        

# write a program to print multiplication table of n using for loop in reversed order.

# n=int(input("enter your number: "))
# for i in range(10,0,-1):
#     print(n,"x",i,"=",i*(n))

# write a program using function to find greatest of three numbers.

# def greatest_num(num1,num2,num3):
#     return max(num1,num2,num3)
# a=int(input("enter your first number: "))
# b=int(input("enter your second number: "))
# c=int(input("enter your third number: "))
# num=greatest_num(a,b,c)
# print("answer",num) 

# def greatest_num(num1,num2,num3):
#     greatest=num1
#     if num2>greatest:
#         greatest=num2
#     if num3>greatest:
#         greatest=num3
#     return greatest        
# a=int(input("enter your first number: "))
# b=int(input("enter your second number: "))
# c=int(input("enter your third number: "))

# greatest=greatest_num(a,b,c)
# print("answer",greatest)

# write a python program using function to convert celsius to fahrenheit.

# def convert(celsius):
#    fahrenheit=(celsius*9/5)+32
#    return fahrenheit
# C=int(input("enter temp. in celsius: "))
# convert(C)
# print("answer",convert(C))    

# how to you prevent a python print() function to print a new line at the end.
# ''' we can a new line by simply using the end='' parameter at the end of the first line  '''

# write a recursive function to calculate the sum of first n natural numbers.

# def sum_first_n_natural_num(n):
#     if n==1:
#         return 1
#     else:
#         return n + sum_first_n_natural_num(n-1)
# n=int(input("enter your number: "))
# print(sum_first_n_natural_num)
    
# write a python funtion to print first n lines of the following pattern. for n=3
#  * * *
#  * *
#  *

# n=3
# def star_pattern(n):
#     for x in range(n,0,-1):
#      print(''," * "*(x-n-1),end=" ")
#      print(''," * "*(x))
# star_pattern(n)        

# write a python function which converts inches to cms.
# def converter(n):
#     if n==1:
#         return 2.54
#     else:
#         return 2.54*converter(n-1)
# n=int(input("enter your value: "))
# print(converter(n))

# write  a python function to print mulipltication table of a given number.
# def table(n):
#     for x in range(1,10+1):
#       print(f"{n} x {x} = {n*x}")   
# n=int(input("enter your number: "))
# print(table(n))

# create a class programmer for storing information of few programmers working at microsoft.

# class programmers:
#     def __init__(self,name,employee_id,role):
#         self.name=name
#         self.employee_id=employee_id
#         self.role=role
#         self.compamy="microsoft"
#     def dispaly_info(self):
#         print(f"name:{self.name}")
#         print(f"employee:{self.employee_id}")
#         print(f"role:{self.role}")
#         print(f"company:{self.compamy}")
#         print()
# progg1=programmers("yogesh",1234,"software engineer")
# progg2=programmers("nav",9876,"HR")
# progg1.dispaly_info()        ,progg2.dispaly_info()


# write a class calculator capable of finding sqaure,cube,and square root o fa number.

# class calculator:
#     def __init__(self):
#      pass
#     def square(self,num):
#        return num**2
#     def cube(self,num):
#        return num**3
#     def squareroot(self,num):
#        return num**0.5
# cal=calculator()
# num=2    
# print(f"square of {num}:",cal.square(num))
# print(f"cube of {num}:",cal.cube(num))
# print(f"squareroot of {num}:",cal.squareroot(num))       

#create a class with a class attribute a ;create an objects from it and set a directly using object.a=0.does this change the class attribute?
# class myclass:
#     n=10
# obj=myclass()
# print("intial class attribute myclass.n: ",myclass.n) 
# print("intial class attribute obj.n:",obj.n)
# obj.n=0
# print("after settting obj.n=0")
# print("class attribute  myclass.n:",myclass.n)
# print("object attribute obj.n:",obj.n)

# write a class calculator capable of finding square,cube and sqaure root of a number.add a static method to greet the user with hello .
# class calculator :
    
#     @staticmethod
#     def greet_user():
#         print("hello user!")
#     def square(self,n):
#         return n**2
#     def cube(self,n):
#         return n**3
#     def square_root(self,n):
#         return n**0.5
# calculator.greet_user()    
# cal=calculator()
# n=2
# print("square of num:",cal.square(n))
# print("cube of num:",cal.cube(n))
# print("square root of num:",cal.square_root(n))    

# write a class train which has methods to book a ticket,get status(no of seats) and get fare information of trains running under indian railways.


# class train :
#     def __init__(self,train_name,total_seats,fare_per_seat):
#         self.train_name=train_name
#         self.total_seats=total_seats
#         self.available_seat=total_seats
#         self.fare_per_seat=fare_per_seat

#     def book_a_ticket(self,num_ticekts):
#         if num_ticekts<=self.available_seat:
#             self.available_seat-=num_ticekts
#             print(f"successfully booked{num_ticekts}tickets for {self.train_name}")
#         else:
#             print(f"sorry,only{self.available_seat} tickets available for {self.train_name}")

#     def get_status(self):
#         print(f"available seats in {self.train_name}:{self.available_seat}/{self.total_seats}")
    
#     def get_fare_info(self):
#         print(f"fare per seat in {self.train_name}: INR {self.fare_per_seat}")

# train1=train("rajdhani express",300,1500)
# train2=train("shatabdi express",200,1200)

# train1.get_status()
# train1.get_fare_info()
# print("")
# train2.get_status()
# train2.get_fare_info()
# print("")
# train1.book_a_ticket(2)
# train1.get_status()
# print("")
# train2.book_a_ticket(2)
# train2.get_status()

# # create a class 2-d vector and use it to create another class representing a 3-d vector.

# class vector2D:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"({self.x},{self.y})"
        
#     def add(self,other):
#         return vector2D(self.x+other.x,self.y+other.y) 
#     def subract(self,other):
#         return vector2D(self.x-other.x,self.y-other.y) 
#     def multiplication(self,scalar):
#         return vector2D(self.x*scalar,self.y*scalar)

# class vector3D(vector2D):
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z=z
    
#     def __str__(self):
#         return f"({self.x},{self.y},{self.z})"
#     def add(self,other):
#         return vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
#     def substract(self,other):
#         return vector3D(self.x-other.x,self.y-other.y,self.z-other.z)
#     def multiplication(self,scalar):
#         return vector3D(self.x*scalar,self.y*scalar,self.z*scalar)
# # v2d1=vector2D(1,2)
# # v2d2=vector2D(3,4)
# # print(f"2D vector: {v2d1}")    
# # print(f"2D vector: {v2d2}"),print("")
# # print("addition:",v2d1.add(v2d2)),print("")
# # print("subraction:",v2d1.subract(v2d2)),print("") 
# # print("multiplication:",v2d1.multiplication(2)),print("")

# v3d1=vector3D(1,2,3)
# v3d2=vector3D(4,5,6)
# print(f"3D vector: {v3d1}")    
# print(f"3D vector: {v3d2}"),print("")
# print("addition:",v3d1.add(v3d2)),print("")
# print("subraction:",v3d1.subract(v3d2)),print("") 
# print("multiplication:",v3d1.multiplication(2)),print("")
    
# # create a class pets from a class animals and further create class dog from pets .add a mewthod bark to class dog .

# class animal:
#     def __init__(self,species):
#         self.species=species
# class pets(animal):
#     def __init__(self,species,name):
#         super().__init__(species)
#         self.name=name
# class dog(pets):
#     def __init__(self,name):
#         super().__init__("dog",name)
#     def bark(self):
#         return "woof!"
# doggy=dog("khajoor")
# print(f"my dog's name is {doggy.name}.he is a {doggy.species}")
# print(f"he says: {doggy.bark()}")    


# create a class employee and add salary and increment properties to it. 
# # write a method salary after increment method with a @property decorator with a settere,
# #  which change which changes the value of increment based on the salary.

# class employee :
#     def __init__(self,name,salary,increment):
#         self.name=name
#         self.salary=salary
#         self.increment=increment
#     @property    
#     def salary_after_increment(self):
#         return self.salary +(self.salary *self.increment/100) 
#     @property
#     def increment_in_salary(self):
#         return self.increment
#     @increment_in_salary.setter
#     def salary_increment(self,new_increment):
#         if new_increment>=0:
#             self.increment=new_increment
#         else:
#             raise ValueError("Increment must be a non-negative value.")
# emp = employee("yogesh",50000,5) 

# print(f"initial salary:INR {emp.salary}")
# print(f"intial increment:{emp.increment}%")
# print(f"salary after increment: INR {emp.salary_after_increment:.2f}"),print()

# emp.increment=7
# print(f"new increment :{emp.increment}%")
# print(f"new salary after increment : INR{emp.salary_after_increment:.2f}")


# write a class complex to represent complex numbers,along with overloaded operators + and * which adds and multiplies them.
# class complex:
#     def __init__(self,real,image):
#         self.real=real
#         self.image=image

#     def __str__(self):
#         return f"{self.real} + {self.image}i"

#     def __add__(self,other):
#         return complex(self.real+other.real ,self.image+other.image)
#     def __mul__(self,other):
#         return complex(self.real*other.real - self.image*other.image ,
#                        self.real*other.real + self.image*other.image)   
# c1=complex(3,2)
# c2=complex(1,7) 

# sum_result =c1+ c2
# print(f"sum: {sum_result}")

# product_result =c1*c2
# print(f"product: {product_result}")

# write a class vector representing a vector of n dimension.overload the + and * operator which calculates the sum and the dot product of them.
# class VECTORS:
#     def __init__(self,*component):
#         self.component=component

#     def __add__ (self,other):
#         if len(self.component)!=len(other.component):
#             raise ValueError("enter the value of same dimension.")
#         sum=tuple(x+y for x,y in zip (self.component,other.component))
#         return VECTORS(sum)
    
#     def __mul__(self,other):
#         if len(self.component)!=len(other.component):
#             raise ValueError("enter the value of same dimension.")
#         dot_product=sum(x*y for x,y in zip (self.component,other.component))
#         return (dot_product)

# v1=VECTORS(1,2,3)
# v2=VECTORS(4,5,6)

# result_sum= v1+v2
# result_dot_product=v1*v2
# print(f"sum of component:{result_sum.component}")
# print(f"dot product:{result_dot_product} ")

# write __str__() method to print the vector as follows: 7i+8j+10k assume vector of dimension 3 for this problem,
# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self,other):
#         return vector(self.x+other.x,self.y+other.y,self.z+other.z)
    
#     def  __mul__(self,other):
#         return vector(self.x*other.x,self.y*other.y,self.z*other.z)
#     def __str__(self):
#         return f"{self.x}i + {self.y}j + {self.z}K"
# v1=vector(1,2,3)
# v2=vector(4,5,6)

# print(f"vector 1 : {v1} ")
# print(f"vector 2 : {v2}"),print()

# sum=v1+v2
# print(f"sum of two vector is {sum}")

# product=v1*v2
# print(f"product of two vector is {product}")

# write a class vector representing a vector of n dimension.overload the + and * operator which calculates the sum and the dot product of them. 
# # overide the len() method on vector to display the dimension of the vactor.
# class vector:
#     def __init__(self,*components):
#         self.components=components
#     def __len__(self):
#         return len(self.components)
#     def __add__(self,other):
#         if len(self.components) !=len(other.components):
#             raise ValueError("enter te same dimension vector")
#         sum=tuple(x+y for x,y in zip(self.components,other.components))
#         return vector(sum)
#     def __mul__(self,other):
#         if len(self.components) !=len(other.components):
#             raise ValueError("enter te same dimension vector")
#         dot_product=sum(x*y for x,y in zip(self.components,other.components))
#         return (dot_product)
# v1=vector(1,2,3)
# v2=vector(4,5,6)

# result_sum= v1+v2
# product=v1*v2
# print(f"sum of two vector: {result_sum.components}")
# print(f"dot product of two vector: {product}")


# write a program to print third,fifth and seventh elemnet from a list using enumerate funtion.

# a=["apple","banana","cherry","kiwi","coconut","watermelon","muskmelon","pear"]
# skip_elem={3,5,7}
# for index, a in enumerate(a):
#     if index in skip_elem:
#         continue
#     print(a)

# write a list comprehension to print a list which contains the multiplication tbale of a user entered number.
# n=int(input("enter your number: "))
# t=[n*i for i in range(10+1)]
# print(f"table: {t}")

# write a program to display a/b where a and b are integers. if b=0,display infinite by handling the Zero Division Error.
# a=int(input("enter your first number: "))
# b=int(input("enter your second number: "))     
# try:
#      result=a/b
#      print(result)
# except ZeroDivisionError:
#      print("Error: Division of zero is not allowed.")     

# write a program to input name ,marks and phone number of a student and format it the format function like below:
# "the name of the student is harry,his marks are 72 and phone number is 99999888"

# n=input("enter your NAME: ")
# m=input("enter your MARKS: ")
# p=input("enter your PHONE NUMBER: ")

# print(f"The name of the student is {n},his marks are {m} and phone number is {p}")

# def info():
#     print(f"'The name of the student is {n},his marks are {m} and phone number is {p}'")
#     return info
# n=input("enter your NAME: ")
# m=input("enter your MARKS: ")
# p=input("enter your PHONE NUMBER: "),print("")

# info()

# A list contains the multiplication table of 7. write a program to convert it to a vertical string of some numbers.
# num=7
# table =list(map(lambda i: f"{num*i}",range(1,10+1)))
# for x in table:
#     print(x)

# num =7
# def mul_table(m):
#     return m*num
# table=list(map(mul_table,range(1,10+1)))
# for x in table:
#  print(x)

# write a program to filter a list of numbers which are divisible by 5.

# a= list(filter(lambda x:x%5,range(1,50+1)))
# print(a)

# def num(n):
#     return n%5
# result=list(filter(num,range(1,20+1)))
# print(result)


# write a program to find the maximum of the number in a list using the reduce function.

# from functools import reduce
# data1=[8,76,5,33,22]
# result1=reduce(lambda x,y: x if x>y else y, data1)
# print(f"your maximum number is {result1}")

# from functools import reduce
# data2=[45,34,3,98,76,46]
# def max_num(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# result2=reduce(max_num,data2)    
# print(f"your maximum number is {result2}")
