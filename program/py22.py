#Create a dictionary to store data (name, roll number) of N students. 
#The key will be the roll number of the student and the value contains the 
#data of the student (in a list). Write a program that asks the user to enter 
#a name of a Student, search it in the dictionary and print the data of the 
#Student if it is available otherwise display an appropriate message.

d={"roll_number":["name","class","Age","hobby"]}
a=int(input("How many student data u want to enter:"))
for i in range (a):
    roll=int(input("Enter roll no.:"))
    name=input("Name of the student:")
    c=input("Enter class:")
    age=int(input("Enter age of the student:"))
    h=input("Enter hobby:")
    d[roll]=[name,c,age,h]
    print()

s=input("Enter name of the student ")
for x,j in d.items():
    if (j[0]==s):
        print(x,j,sep=":")
