#leap year divisible by 4.multiple of 400 and not 100
def checkleapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year=2025
result=checkleapyear(year)
print(result)
