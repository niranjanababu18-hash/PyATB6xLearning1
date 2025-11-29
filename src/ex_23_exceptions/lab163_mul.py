try:
    a=int(input("first"))
    b=int(input("second"))
    c=a/b
    print(c)
except (ZeroDivisionError,TypeError,ValueError):
    print("Error")
#try except else finally