#WAP that will find the roots of a quaduratic equation:ax^2+bx+c=0
 
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

d=(b*b)-4*a*c

if(d>0):
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print("The roots of the equation are:",r1,"and",r2)
elif(d==0):
    r1=(-b+(d**0.5))/(2*a)
    print("The roots of the equation are:",r1)
else:
    print("The roots of the equation are imaginary")
