class Patient:
    def __init__(self):
        self._id=None
        self._name=None
        self._ssn=None
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_ssn(self):
        return self._ssn
    def set_id(self,id):
        self._id = id
    def set_name(self,name):
        self._name = name
    def set_ssn(self,ssn):
        self._ssn = ssn

n=Patient()
n.set_name("Patient")
n.set_ssn("2132")
n.set_id("2132")
print(n.get_id())
