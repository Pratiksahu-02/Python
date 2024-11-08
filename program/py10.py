# WAP that will print the odd numbers from n1 to n2 
# where the value of n1 and n2 are enter by user.
n1=[]
n=int(input("Enter how many number you want to add in list:"))
n2=[]
for i in range(n,0,-1):
    a=int(input("Enter a number:"))
    n1.append(a)
for i in n1:
    if (i%2!=0):
        n2.append(i)
print(n2)