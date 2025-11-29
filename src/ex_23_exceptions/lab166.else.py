try:
    a=int(input("first"))
    b=int(input("second"))
    c=a/b
    print(c)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Division Error")
except TypeError:
    print("Type Error")
else:
    print("No Error")
finally:
    print("Finally-always will be executed")
#try except else finally