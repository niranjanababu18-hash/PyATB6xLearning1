key={1,2,3}
value={"Niranjana","neeraj","Nishanth"}
dict1=dict(zip(key,value))
#zip-creating dict
print(dict1)
#print(dict.get(1))
#creation -secodn method
student_list=dict(name="niranjana",age=34)
merged_dict=dict1|student_list
print(merged_dict)