#go for match if multiple conditions are coming.no concept of switch in python
test=str(input("enter which type of test you need :API,REGRESSION,SIT,DEV\n")).upper().strip()
match test:
    case "API":
        print("Please run API Test")
    case "REGRESSION":
        print("Please run REGRESSION Test")
    case "SIT":
        print("Please run SIT Test")
    case "DEV":
        print("Please run DEV Test")
    case _:
        print("Please enter valid input")
