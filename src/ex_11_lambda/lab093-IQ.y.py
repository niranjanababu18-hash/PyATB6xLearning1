num=int(input("print the number"))
check_user=lambda num:"even" if num%2==0 else "odd"
result=check_user(num)
print(result)