#Sequence cahracter
#\d: digiti charater
#\D: Non digit
#s:spance \s:opposite of s
#\A: serach or string
#\Z:At the end
#\w: alphaneumeric character
import re
str="TAke1 up one 22-11-2012 2idea at3 a tim4e, one"
#gives the first string matches the regex pattern
result=re.search(r'o\w\w',str)
print(result.group())

#find all (in form of list) string matches 
result=re.findall(r'o\w\w',str)
print(result)

#search at the beginign of the string
result=re.match(r'T\w\w',str)
print(result)

#split using regex pattern
result=re.split(r'\d+',str)
print(result)

#substitute
result=re.sub(r'one','two',str)
print(result)

#+:one or more characters
#{m}:m occruance
#{m,n} : m:min occrances, n:max occrances
#?: one occurrence

result=re.findall(r'o\w+',str)
print(result)

result=re.findall(r'o\w{2}',str)
print(result)


result=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

#Sperical caharacter 
