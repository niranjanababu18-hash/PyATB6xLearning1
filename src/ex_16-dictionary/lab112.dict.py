dict={
    "name":"niranjana",
    "age":34,
    "age": 31,
    "place":"payyanur"
    }
#print(dict['name'])
dict['experience']=9
print(dict)
#age is duplicate .not taken second value taken
del dict['experience']
#print(dict)
for key,value in dict.items():
    print(key)
print("age" in dict)
print("address" in dict)
dict['age']=30
print(dict)