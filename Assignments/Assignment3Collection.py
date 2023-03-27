
# Assignment using List
print("Assignment using List")
print("================================================")
countryList=["India", "Japan", "USA"]
print(countryList)
countryList.append("Canada")
print(countryList)
countryList.remove(countryList[2])
print(countryList)
print(len(countryList))
# countryList.index(2,"Germany")
countryList=countryList[0:1]+["Germany"]+countryList[1:]
print(countryList)

# Assignment Using SEts
print("Assignment Using Sets")
print("================================================================")
countrySet={"India", "Japan", "USA"}
print(countrySet)
countrySet.update(["Canada"])
print(countrySet)
countrySet.remove("Japan")
print(countrySet)
countrySet=countrySet[0:1]+{"Canada"}+countrySet[1:]
print(countrySet)

