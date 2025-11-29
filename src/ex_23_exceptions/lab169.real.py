import requests
try:
    url=input("enter url")
#    response=requests.get('http://api.example.com/data')
    response=requests.get(url)
    print(response.status_code)
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.Timeout:
    print("Timeout error")
except Exception as e:
    print(e)