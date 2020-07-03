import copy
class TestClass:
    def changeI(self, newI):
        self.i = newI
    def __init__(self, test):
        self.i = test
c = TestClass(8)
d = copy.deepcopy(c)
d.changeI(4)
print(c.i)
print(d.i)