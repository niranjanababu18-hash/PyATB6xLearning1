#reading a file
import os
full_path=os.path.join("/Users/neenu/PycharmProjects/PyATB6xLearning1/src/ex_26_collections/testdata.txt")
print(full_path)
file=open(full_path,'r')#opening in read mode
print(file.read())