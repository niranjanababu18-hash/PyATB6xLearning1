##strip-copies string without spaces
age=int(input("enter age\n").strip())
if age<=0 or age>130:
    print("Enter valid age")
else:
      if age>21:
        print("You are old enough")
      elif age==21:
        print("With parents")
      else:
        print("Not allowed")
