n=int(input("Enter a number:"))
i=n
r=0
s=0
while(n>0):
    r=n%10
    s=s+(r**3)
    n=n//10
print(i)
print(s)