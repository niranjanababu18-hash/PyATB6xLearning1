my_list=[1,2,3]
#my_list[0]=-2
#my_list[1]=-1
#print(my_list)
#for item in my_list:
 #   print(item)
#for i in range(0,3):
 #   print(my_list[i])
my_list.append(4)
#append to last index
#print(my_list)
#extend to add to another list
my_list1=[5,6,7]
my_list.extend(my_list1)
#print(my_list)
#insert to required index
my_list.insert(0,-1)
my_list.append('end')
my_list[0]='Niranjana'
my_list.remove('Niranjana')
#print(my_list)
my_list_copy=my_list.copy()
my_list_copy.insert(1,"Babu")
print(my_list_copy)

