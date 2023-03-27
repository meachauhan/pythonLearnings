#can't be modified
#Immutable
# Insertion order is maintained
# for single tuple add , at last

tpl=(20,30,40,"String")
print(tpl)
print(type(tpl))

tp1=(20,)
print(tp1)

print(tpl*3)
print(tpl.count(20))
print(tpl.index(20))


# Converting list to tuple
list=[10,20,"alkas"]
tple=tuple(list)
print(tple)

