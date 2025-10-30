def validation(response_code):
    if response_code == 200:
        print("Request placed successfully")
    else:
        print("Request stuck")
print("I need to validate the request status")
response_code=int(input("enter response code"))
if response_code>0:
    validation(response_code)
else:
    print("Fail")