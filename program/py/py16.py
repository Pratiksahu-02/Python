#WAP that will add two square matrices. 
#The dimension and elements of the matrices will be entered by the user.

a=int(input("Enter size of square matrices(2x2or3x3)only write(2-3):"))
l1=[]
l2=[]
l3=[]
print("Matrice 1")
for i in range(a):
    for j in range(a):
        n=int(input("Enter a number:"))
        l1.append(n)
print("Matrice 2")
for i in range(a):
    for j in range(a):
        n=int(input("Enter a number:"))
        l2.append(n)
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
    
l3.reverse()
print("[")
for i in range(a):
    for j in range(a):
       print(l3.pop(),end=(" "))
    print()
print("]")