#find the maximum between 3 numbers
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))
if a>=b and a>=c:
    print("max is ",a)
elif b>c and b>a:
    print("max is ",b)
else:
    print("max is ",c)