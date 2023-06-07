class BMW:
    
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Start parent class")
class ThreeSeries(BMW):
    def start(self):
        print("Start child class")
    def __init__(self,curiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.curiseControlEnabled=curiseControlEnabled 
class FiveSeries(BMW):
     def __init__(self,parkingAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingAssistEnabled=parkingAssistEnabled

threeseries=ThreeSeries(True,"BMW","328i","2018")
print(threeseries.curiseControlEnabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
threeseries.start()