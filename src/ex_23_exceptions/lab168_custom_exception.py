class invalidageError(Exception):
    pass
def validate(age):
    if age >= 18:
        print("Approved")
    else:
        raise Exception("Invalid age")
validate(8)