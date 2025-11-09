dict1={
    "name":"niranjana",
    "age":34,
    "age": 31,
    "place":"payyanur"
    }
dict2=dict={
    "name":"neeraj",
    "age": 33,
    "place":"chalakudy"
    }
student3=dict1={
    "name":"niranjana",
    "age":34,
    "age": 31,
    "place":{
                "District":"kannur",
                "municipality":"payyanur"}
    }
print(student3["place"]["municipality"])
studentlist=[dict1,dict2,student3]
print(studentlist)
print(studentlist[2]['place']['municipality'])
