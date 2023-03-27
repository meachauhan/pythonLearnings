math=int(input("Enter the math marks:"))
physics=int(input("Enter the physics marks:"))
chemistry=int(input("Enter the chemistry marks:"))

if(math>=35 and physics>=35 and chemistry>=35):
    average=(math+physics+chemistry)/3
    if(average<=59): print("your grade is C")
    elif(average<=69): print("your grade is B")
    else: print("your grade is A")
    
else:
    print("You have failed the exam")
    


