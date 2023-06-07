from datetime import *
class Address:
    def __init__(self, street, city, state,country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
    def displayAddress(self):
        print("Addres is:",self.street," ",self.city," ",self.state," ",self.country," ",self.zipcode)
class venue:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def displayVenue(self):
        print("Venue is:",self.name," ",self.address.displayAddress())
class Event:
    def __init__(self,start,end,venue):
        self.start = start
        self.end = end
        self.venue = venue
    def displayEvent(self):
        print("Event is:",self.start," ",self.venue.displayVenue())

a=Address("Niladri Nagar","Electronic city","Karnatakan","India","211223")
v=venue("Food Resstorant ",a)
st=datetime.today()
d=date(2042,7,21)
t=time(12,45)
et=datetime.combine(d,t)
e=Event(st,et,v)
e.displayEvent()
