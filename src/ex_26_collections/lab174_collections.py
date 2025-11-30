from collections import *
#user_input=input("Enter a string: ")
#counter is a data structure inside module colections
#count_char=Counter(user_input)
#print(count_char)
test=namedtuple("info",field_names="name,age,ismarried,marks")
t=test("babu",34,True,9.8)
print(t.name)
print((t.ismarried))