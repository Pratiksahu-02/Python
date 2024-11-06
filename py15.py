#WAP to ask the data of five students that contain name, roll number, age. 
#Sort the list based on roll number of the Student. [Note: Use list of lists].

print("Enter data of 5 student:")
l=[]
for i in range(1,3):
    print("Enter data of",i,"student")
    name=input("Enter name of the student:")
    roll=int(input("Enter roll number:"))
    age=int(input("Enter age of the student:"))
    c=[name,roll,age]
    l.append(c)
print(l)