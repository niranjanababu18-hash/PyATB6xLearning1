dict1={"a":1 ,"b":2,"c":3}
dict2={"a":1 ,"b":2}
missing_keys=dict1.keys()-dict2.keys()
#find difference in json
print(missing_keys)