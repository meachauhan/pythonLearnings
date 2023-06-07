#Duck Typing
class Duck:
    def talk(self):
        print("Quack Quack!")
class Human:
    def talk(self):
        print("Human!")

def callTalk(object):
    object.talk()
    
duck = Duck()
callTalk(duck)
human=Human()
callTalk(human)