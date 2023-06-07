import sys

lst=sys.argv
accBalance=10000

if lst[1]=="1":
    print("your curren account balance is " + str(accBalance))
elif lst[1]=="2":
    amt=int(input("Please enter amount to withdraw:"))
    if(amt>accBalance): 
        print("your account balance is " + str(accBalance))
        print("Please use less than that ammount to withdraw")
    else:
        accBalance-=amt
        print("successfully withdraw"+str(amt))
        print("your account balance is " + str(accBalance))
elif lst[1]=="3":
    amt=int(input("Please enter amount to cash diposit:"))
    accBalance+=amt
    print("Amount Deposited successfully")
    print("your account balance is " + str(accBalance))
elif lst[1]=="4":
    amt=int(input("Please enter amount to cheque deposit:"))
    accBalance+=amt
    print("Amount Deposited successfully")
    print("your account balance is " + str(accBalance))
else:
    print("Please enter valid Option")
