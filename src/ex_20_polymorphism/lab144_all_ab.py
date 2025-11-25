class person:
    def say_name(self,name):
        self.name=name
        print("hi",self.name)
    def say_name(self,name,second_name):
        print("my name is ",name,second_name)
abc=person()
abc.say_name("John","dennis")
#taking maximum arguments method


