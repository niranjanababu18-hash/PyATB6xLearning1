#filter elements based on a condition
listnum=[1,2,3,4,5,6,7,8,9,10,11,12]
def even(x):
    if x%2==0:
        return x
print(list(filter(even,listnum)))
