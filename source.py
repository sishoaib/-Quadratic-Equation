#To find the root to the quadratic equations
import cmath
import math
a = int (input("Enter the value of 'a' : "))
b = int (input("Enter the value of 'b' : "))
c = int (input("Enter the value of 'c' : "))
d =(b**2) - (4*a*c)
if(d==0):
x1= -b/(2*a)
    print("X = ",x1)
elif(d>0):
    x1= (-b + math.sqrt(d))/(2*a)
    x2= (-b - math.sqrt(d))/(2*a)
    print("X = (",x1,",",x2,")")
elif(d<0):
    x1= (-b + cmath.sqrt(d))/(2*a)
    x2= (-b - cmath.sqrt(d))/(2*a)
    print("X = (",x1,",",x2,")")
