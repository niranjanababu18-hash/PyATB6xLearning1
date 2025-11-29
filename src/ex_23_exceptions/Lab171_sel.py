try:
    data=open("test.json").read()
except FileNotFoundError as e:
    print(e)
finally:
    print("clean")
#f,e=alias