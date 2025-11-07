def checkui(func):
    def wrapper():
        print('checkui before running')
        func()
        print('checkui after running')
    return wrapper

@checkui
def uitest():
    print('uitest function')
uitest()