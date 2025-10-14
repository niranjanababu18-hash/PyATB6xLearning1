#write a python program to calculate are of circle
#area=pi*r*2
#take pi=3.14
#take radius as input
#using math function
import math

r=float(input("Enter radius of circle"))
a=math.pi*pow(r,2)
print(f"Area of circle is :{a:.2f}")
#STRING DATA FORMATTING /formatted string literals TO 2 DECIMAL-a:.2f ->f"area is : {a:.2f}"
#print("area is :",a)

