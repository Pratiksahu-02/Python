# WAP to print to find the factorial values of a number enter by user>\.
#Factorial = n! = 1*2*3*.......*n
n=int(input("enter the which you want to find the factorial"))
mul=1
for i in range(1,n+1):
    mul=mul*i
print(("factorial of ",n," is ",mul))