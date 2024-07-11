name= 'yogesh kumar'
rollno = "78"
fees=5600
result='my name is {0} and my rollno is {1} and thankyou {0}'.format(name,rollno)

result_2='my name is{}and my rollno is{}'.format(name,rollno)
result_3= f"my name is {name} and my rollno is {rollno}"
result_4= 'my name is {%s} and my rollno is {%s}'.format(name,rollno)
print(result)
print(result_2)
print(result_3)
print(result_4)