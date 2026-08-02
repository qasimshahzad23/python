# simple code in the py
print("hello world")
sum=2+4
print(sum)
# operator in py
print(2+4)
print(2-4)
print(2*4)
print(2/4)
print(2%4)
print(2**4)
# comment in the python 
print("the # symbole is used for comment in python")
# input variable in python
# input for the string 
name =input("enter your name:")
print("hello",name)
print("hello"+name)
# input for the integer
num = int (input("enter the number you want to print:"))
print("the number you entered is:", num)
# print("the number you entered is "  num)
print("the number you entered is:"+str(num))
# condional logic in the python
print(4==6)
print(4!=6)
print(4>6)
print(4<6)
print(4>=6)
print(4<=6)
# type conversion in 
sum=2+4
print(sum)
print ("the type of sum is:",type(sum))
sum=float(sum)
print("the type of sum is:",type(sum))
sum=str(sum)
print("the type of sum is:",type(sum))

# if else and elif in python
x=10 
if (x<10):
    print("the value of x is less than or equal to 10",x)
elif (x>10):
    print("the value of x is greater than 10",x)
else:
    print("the value of x is equal to 10  ",x)
# function in python
def sum():
    sum=2+4
    print("the sum of 2 and 4 is:",sum)
sum()
def add():
    sum=2+4
    return sum
new_result=add()
print("the sum of 2 and 4 is:",new_result)
# loops in python
# while loop in python
x=0
while (x<10):
    print("the value of x is:",x)
    x+=1   
# forloop in the python
for i in range(4,12):
    print("the value of i is:",i)
# some important linbraries in python
import math
print("the value of pi is:",math.pi)
print("the value of e is:",math.pow(2,3))
print("some important libraries in python are:","numpy","pandas","matplotlib","seaborn","scikit-learn")
# error typer in the py
# syntax error
# runtime error
# logical error
# symatic error
print("syntax error, runtime error, logical error, semantic error are the types of error in python")