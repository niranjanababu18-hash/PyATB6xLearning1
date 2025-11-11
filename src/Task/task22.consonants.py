#find consonents in dict
string="hello world"
vowels="aeiou"
vowels_count=0
consonant_count=0
#result=dict()
for char in string:
    if char not in vowels:
        consonant_count+=1
 #       result[char]=vowels_count
print("count of consonants",consonant_count)
#print(result)

for char in string:
    if char in vowels:
        vowels_count+=1
print("count of vowels",vowels_count)
