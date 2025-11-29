a=int(input("first"))
b=int(input("second"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("division by zero")
#try except else finally