class person:
    name=None
    id=None
    age=None
  #inside class-method
    def talk(self):
        print('talk')
    def sleep(self,name):
        print('sleep',name)
    def jump(self,name):
        print('jump',name)
        return None
#outside class-function
def function_walk(self):
    print('function-walk')
