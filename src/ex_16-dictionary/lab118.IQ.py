my_dict={"a":1,"b":2,"c":3,"d":1,"e":5,"f":6}
#find duplicate values
unique_value=set()
result={}
for key,value in my_dict.items():
    if value not in unique_value:
        result[key]=value
        unique_value.add(value)
print(result)