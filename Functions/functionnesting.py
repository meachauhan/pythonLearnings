def display(name):
    #scope is inside only in the function scope
    def message():
        return "Hello"
    result= message()+name
    return result
print(display("Akash"))


