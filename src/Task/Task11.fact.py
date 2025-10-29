#factorial
#Question 1:Given a  number you need to calculate the factorial of that number
num=int(input("enter number"))
fact=1
if num<=0:
    print("fact is ", fact)
else:
    for i in range(1,num+1):
        fact=fact*i
print("factorial is: ",fact)