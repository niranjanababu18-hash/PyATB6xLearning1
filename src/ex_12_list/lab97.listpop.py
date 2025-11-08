#pop removes last element
from operator import index
my_list=[1,2,3,4]
my_list.pop()
#not specified last element will be removed.else we can specify index
#remove specifying which value to be removed
#print(my_list)
#my_list.clear()
print(my_list.index(2))
my_list.reverse()
my_list.sort(reverse=True)
#reverse sort
print(my_list)
count=my_list.count(7)
print(count)
print(max(my_list))
print(min(my_list))
print(sum(my_list))
#slicing
print(my_list[2:3])
#LIST CREATION AND COMPREHENSION
L=list(range(10))
print(L)
#list of list
list=[[1,2,3],[4,5,6],[7,8,9]]
del list[0]
#del is a keyword not like pop which is a functioni
print(list)
#delete never returns any element.pop removes it

