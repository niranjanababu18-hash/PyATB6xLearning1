#we can move from one package to package
#module is python file inside a package
#which can be imported from location to another
#module can be directly imported.but package -need to use -->from package import *
#package vs directory vs module
#dire-just a folder-not shared
#when they contain a special file-__init__ --> it is promoted to the package by python
#advantage is you can import and export easily
import mymodule
print(mymodule.greet("world"))
