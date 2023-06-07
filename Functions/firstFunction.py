#function to give average of two numbers
def average(a, b):
    print("Average of two numbers is: ",(a+b)/2)
average (20,90)

#function with return statement

def average_return(a, b):
    return (a+b)/2
print("Average of two numnber is: ",average_return(20,90))

#multiple return statements
#making calulator
def cal(a, b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u
result=cal(10,30)
#keyword as argument ordering doesn't matter
print(cal(a=10,b=20))
print (result)


def fun(lst=[2,3]): #funstion with default values
    for i in lst: print(i)

fun([1,2,3,4,5])

#Default agruments

# fun() will give error
fun()


#Optional arguments
#*args contain any number of arguments storing in the tuple
#**kwargs contains any number of keyword arguments storing in the tuple
def myfun(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

myfun(10,20,name="Akash",sal=1000)