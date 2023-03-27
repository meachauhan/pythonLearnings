# Single Line String
s="You are awesome!"
print(s)

# Multiline String
s1="""You are creatore of 
your destination"""
print(s1)

# Indexing
print(s[0])

# repetation
print(s*3)

# Length Operations
print(len(s))


# slicing : endign index won't be included 
print(s[0:5])

# Go till end of string
print(s[5:])

# Step values
print(s[0:9:2])

# reversing the String
print(s[::-1])


# Strip function:remove extra spaces have variant as lstrip() and rstrip()
print(s.strip()) 

print(s.find("awe" ,0,len(s))) #finding the substring function
print(s.count("a")) # count occrance of the substring function
print(s.replace("awesome","super"))

print(s.upper())
print(s.lower())
print(s.title())
