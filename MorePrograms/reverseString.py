s="djfajdf"
print(''.join(reversed(s)))

str="All the power is with in you"
temp=str.split()
print(temp)
result=[]
i=len(temp)-1
while i>=0:
    result.append(temp[i])
    i=i-1
print(result)
output=' '.join(result)
print(output)

str2="All the power is with in you"
temp1=str2.split()
result2=[]
o=0
while o<len(temp1):
    result2.append(temp1[o][::-1])
    o=o+1
print(result2)
print(' '.join(result2))


str3="akash"
#Removing the characrer from the string

result3=[]
for c in str3:
    if c not in result3:
        result3.append(c)
print(''.join(result3))

#Occurance of the characters in the string

result4={}
for c in str3:
    if c in result4.keys():
        result4[c]=result4[c]+1
    else:
        result4[c]=1

print(result4)
for k,v in result4.items():
    print('{}={} times'.format(k,v))
    