#WAP to ask the data of five students that contain name, roll number, age. 
#Sort the list based on roll number of the Student. [Note: Use list of lists].

print("Enter data of 5 student:")
l=[]
for i in range(1,6):
    print("Enter data of",i,"student")
    name=input("Enter name of the student:")
    roll=int(input("Enter roll number:"))
    age=int(input("Enter age of the student:"))
    c=[roll,name,age]
    l.append(c)
print(["Roll","Name","Age"])
l.sort()
print(l)