class Parent:
    def a1(self):
        print("A1")
    def a2(self):
        print("A2")
class Child(Parent):
    def b1(self):
        print("B1")
    def b2(self):
        print("B2")

c = Parent()
c.a1()
c.a2()
c.b1()
c.b2()