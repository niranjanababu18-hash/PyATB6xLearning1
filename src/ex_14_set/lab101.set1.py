#set is an unordered collection of data immutable,iterable not allowing duplicates
#curly braces
set1={1,2,3,1,4,5,6,6,7,True}
print(set1)
#TRUE NOT PRINTED BECUASE-SET NOT ALLOWING DUPLICATES AND IN PYTHON TRUE=1
print(len(set1))
t=(1,2,3,'neenu')
t=set(t)
print(t)
t.add(4)
t.remove(4)
#print(type(t))


