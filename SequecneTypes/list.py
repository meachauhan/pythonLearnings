lst=[]
print(lst)

lst1=[10,20,"Striong",32.3]
print(lst1)
print(lst1[3])
print(lst1[0:1])
print(lst1*4)
print(len(lst1))

# Adding the element
lst1.append("Alasj")

print(lst1)

# Removing the element
lst1.remove("Alasj")
del(lst1[2])
print(lst1)

print(max(lst1) )
print(min(lst1))
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)

# lst1.clear()
print(lst1)