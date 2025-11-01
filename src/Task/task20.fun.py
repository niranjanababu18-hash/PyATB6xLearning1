def check_status(status):
    match status:
        case 200:
         print("PASS")
        case 400:
            print("FAIL")
        case 500:
            print("FAIL")
        case _:
            print("UNKNOWN")
status= int(input("input status"))
check_status(status)