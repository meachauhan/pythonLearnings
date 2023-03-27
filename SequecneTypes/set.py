s={10,20,10,"Stringss"}
print(s)
print(type(s))
s.update([10,50])
print(s)
#slicing not allowed
#repetation not allowed
#not allowed duplication
#indexing not allowed

f=frozenset(s)
# f.update([90])  frozen set can't be modified

