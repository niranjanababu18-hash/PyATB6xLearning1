#take 3 values where length of traingle
#print type of triangle
def type(a,b,c):
    if a==b and a!=c:
        print("Isosceles")
    elif a==b and a==c:
        print("Equilateral")
    elif a!=b and b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
a=int(input("enter side1"))
b=int(input("enter side2"))
c=int(input("enter side3"))
print("Type of triangle is:")
type(a,b,c)
