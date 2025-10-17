#grade calculator
#A:90-100
#B:80-89
#C:70-79
#D:60-69
#F-<60
score=int(input("enter marks").strip())
#o/p str
if score<0 or score>100:
        print("Enter valid marks")
else:
        if score>=90 and score<=100:
            print("Grade is A")
        elif score>=80 and score<=89:
             print("Grade is B")
        elif score>=70 and score<=79:
             print("Grade is C")
        elif score>=60 and score<=69:
             print("grade is D")
        else:
            print("Fail")