#map applies function to each item in a list or any iterable and returns map object or iterator
numbers=[1,2,3,4]
def power(x):
    return x**2
sq_numbers=set(map(power,numbers))
#mapping function to a set or list or tuple
print(sq_numbers)
