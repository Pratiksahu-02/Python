# WAP that will print the odd numbers from n1 to n2 
# where the value of n1 and n2 are enter by user.
n1=int(input("Enter the starting of the loop:"))
n2=int(input("Enter the ending of the loop:"))
print("Odd number between",n1,"And",n2,"Are:")
for i in range(n1,n2+1):
    if i%2!=0:
        print(i)