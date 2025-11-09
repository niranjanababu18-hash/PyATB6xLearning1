#find the first non repeating charcter in the set
def nonrepeat(string):
    for char in string:
        if string.count(char)==1:
            return char
print(nonrepeat("niranjana"))