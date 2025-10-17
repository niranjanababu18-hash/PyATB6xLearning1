#check if login successful or not
name=str(input("Enter your username\t")).strip().lower()
pwd=str(input("Enter your password\t")).strip().lower()
username="admin"
password="1234"
if username==name and password==pwd:
    print("✅ Login Successful")
else:
    print(" ❌ Invalid Credentials")
