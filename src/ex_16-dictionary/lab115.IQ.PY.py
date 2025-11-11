#frequency of character and creatimg a dict based on that
string="automation"
char_count={}
for char in string:
    char_count[char]=char_count.get(char,0)+1
print(char_count)