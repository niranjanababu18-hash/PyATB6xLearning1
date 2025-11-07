#decorators are a way to modify a function without changing the source code
def addsecurity(func):
    def wrapper():
        print('wear helmet')
        func()
        print('check license and tyre')
    return wrapper

@addsecurity
#@addsecuirty-annotation
def drive ():
    print('drive function')
drive()
#func is a parameter used to call calling function