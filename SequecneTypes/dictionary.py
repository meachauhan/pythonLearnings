dict1={1:"String1", 2:10}
print(dict1)
v=dict1.values()
for i in v: print(i)
print()
print(dict1.items())
k=dict1.keys()
for i in k:
    print(i)

del dict1[1]
print(dict1)
