def outerfunction():
    var1=30
#var1 becomes global var to inner functions.becuase innerfunctions inside outside fucntion
    def innerfunction1():
        print(var1)
        var2=50
        print(var2)
    def innerfunction2():
        print(var1)
    innerfunction2()
    innerfunction1()
outerfunction()