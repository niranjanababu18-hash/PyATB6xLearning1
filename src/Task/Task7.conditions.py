#Accepting response from script and check for APi request and response
response_code=int(input("response code:"))
if response_code==200:
    print("successful request")
elif response_code==404:
    print("Failed API request")
else:
    print("Error")