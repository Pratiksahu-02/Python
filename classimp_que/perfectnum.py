n=int(input("Enter a number:"))
i=n-1
sum=0
while(i>0):
    if n%i==0:
        sum=sum+i
    i=i-1
if (n==sum):
    print("Perfect Number")
else:
    print("Not A Perfect Number")