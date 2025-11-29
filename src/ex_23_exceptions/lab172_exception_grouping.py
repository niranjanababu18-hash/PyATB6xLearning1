eg=ExceptionGroup("Multiple exceptions",[
    ValueError("invalid value"),
    TypeError("invalid type"),
    ZeroDivisionError("division by zero"),
])
def check(a,b):
    b=10
    return b/a
    if a==0:
        raise eg
print(check(0,10))