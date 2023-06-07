class Course:
    noOfObjects=0
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
        Course.noOfObjects+=1
    #Instacne method
    def average(self):
        noOfratigns=len(self.ratings)
        average=sum(self.ratings)/noOfratigns
        print("Average Ratings for ", self.name,"is ",average)
    #getter and setter
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getRatings(self):
        return self.ratings
    def setRatings(self, ratings):
        self.ratings = ratings
    def displayCount():
        print("Count: ",Course.noOfObjects)
c1=Course("MathCuorse",[10,7,5,3])

print(c1.name)
print(c1.ratings)
c1.average()
c1.displayCount()
# c2=Course()
# c2.setName("MathCuorse")
# c2.ratings([0,5,6])
# c2.average()