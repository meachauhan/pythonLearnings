for i in range(5,15):
    if i==10: break
    print (i)

for i in range(5,15):
    if i%3==0: continue
    print (i)
    
x=int(input("eneter a number greater than 10"))
assert x>10, "Wrong number Enetered"
print("U entered", x)