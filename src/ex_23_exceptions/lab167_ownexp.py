def login(username):
    if username == 'admin':
        print("You are logged in as admin")
    else:
        raise Exception("Invalid username")
#own exception creation
print(login('abc123'))