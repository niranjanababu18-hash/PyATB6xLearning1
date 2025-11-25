#static variables or mrthods are shared by all objects of a class
#they belong to class itself ,not to any particular object instance.
class testcounter:
    count=0
    def __init__(self):
        testcounter.count+=1
t1=testcounter()
t2=testcounter()
print(testcounter.count)
