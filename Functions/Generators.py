#returns the squece of values : similar to range fucntions
#yield
def customGen(x,y):
    while x<y:
        yield x
        x+=1
        
for i in customGen(1,10):
    print(i)
