#Create an empty set. 
#Write a program that adds five student names to this set, 
#modifies one existing name, and deletes two names existing in it. 
#[ask the user which name to modify/delete].

students = set()
for i in range(5):
    students.add(input("Enter student name: "))
print("Students: ", students)
name = input("Enter the name to modify: ")
if name in students:
    students.remove(name)
    students.add(input("Enter the new name: "))
print("Students: ", students)
name = input("Enter the name to delete: ")
if name in students:
    students.remove(name)
print("Students: ", students)
