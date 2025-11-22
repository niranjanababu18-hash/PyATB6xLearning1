class mother:
    def money(self):
        print("M1 money")
class father:
    def money(self):
        print("f1 money")
class child(father,mother):
    def run(self):
        print("child")
        self.money()
test=child()
test.run()
#MRO-METHOD RESOLUTION ORDER-ORDER IN WHICH PYTHON SEARCHES A METHOD OR ATTRIBUTE WHEN MULTIPLE INHERITANCE IS USED