class Product:
    def __init__(self):
        self.name ='SAmsung'
        self.description ='Its good'
        self.price = 400
        #Private properties
        self.__id='100'
    def displayId(self):
        print(self.__id)
p1=Product()
print(p1.name)
print(p1.description)
print(p1.price)
p1.displayId()
print(p1._Product__id)