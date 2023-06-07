# w: write mode
#r: read mode
#a :append mode
#x: exclusice creation mode new file will be created if file exists error will be thrown
import os,sys

if os.path.exists('myfile.txt'):
    
    #Opening the file for writing
    f=open("myfile.txt","w")
    print("Enter text (type # when you are done)")
    s=''
    while s!='#':
        s=input()
        f.write(s+"\n")
    f.close()
else:
    print("FIle does not exist")
    sys.exit()
#Opening file in reading mode
f=open("myfile.txt","r")
s=f.read()
print(s)
f.close()