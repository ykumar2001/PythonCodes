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