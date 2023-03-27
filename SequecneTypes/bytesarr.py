li=[20,30,50,244]
print(type(li))
b=bytes(li)
print(type(b))
#can't modify the bytes object 

b1=bytearray(li)
print(type(b1))
b1[2]=22