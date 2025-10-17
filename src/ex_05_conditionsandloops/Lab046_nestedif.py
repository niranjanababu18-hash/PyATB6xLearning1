#find number is even or odd
a=int(input("Enter a number: \n").strip())
if a>=0:
    if a%2==0:
        print("Even")
    else:
         print("odd")
else:
    print("Number is negative")