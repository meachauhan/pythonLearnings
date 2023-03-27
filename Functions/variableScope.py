#global variable
x=123

def display():
    
    #local variable
    x=29
    print(x)
    #accessing global variable with same name as local variable
    print(globals()['x'])
display()

#assinging function to variable
z=display
z()