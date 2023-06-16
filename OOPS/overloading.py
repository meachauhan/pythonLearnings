class Calculate:
   def add(self, a, b, c = 0):
     if c > 0:
         print("a + b + c = {}".format(a + b + c))
     else:
         print("a + b = {}".format(a + b))

c1 = Calculate()
c1.add(10, 20, 30)
c1.add(10,20) 