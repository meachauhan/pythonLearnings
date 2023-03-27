print("Select three topings: ")
print(" 1.Onion \n 2.Lattice \n 3.Tomato \n 4.Olive \n 5.Pepper \n 6.Pickle \n")
list=[x for x in input("Pick three topings: ").split(",")]

noOfSandwitch=int(input("How many sandwitch: "))
print("Total payable amount is: ",noOfSandwitch*5,"$")
