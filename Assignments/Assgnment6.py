n=int(input("Enter any number:"))
for i in range(n):
    if i%10==0: continue
    elif i>100:break
    else:print(i)