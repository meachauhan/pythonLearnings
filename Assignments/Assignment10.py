from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass
class HP(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling from hp")
class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling from Dell")

class HPNoteBook(HP):
    def click(self):
        print("Clicking from HP notebook")
class DellNoteBook(Dell):
    def click(self):
        print("Clcking from Dell notebook")

h=HPNoteBook()
h.click()
h.scroll()
d=DellNoteBook()
d.click()
d.scroll()
    