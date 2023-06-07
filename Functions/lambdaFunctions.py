#lambda argument_list:expression
def cube(a):return a**3
print(cube(3))

f=lambda n:n**3
print(f(9))

#even or odd using lambda argument
f=lambda x: 'YES' if x%2==0 else 'NO'

print(f(9))

#sumof two numbers

k=lambda x,y: x+y
print(k(9,10))