t=open("testdata.txt",'r')
t.close()
#automatically close
with open("testdata.txt","r") as file:
    data=file.read()
    print(data)