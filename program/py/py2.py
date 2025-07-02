#WAP that makes use off trigonometric functions avilable in math module.
from math import *
print("Which oppration you want to preform(choice list)")
print("1.Square root")
print("2.Power")
print("3.Ceil")
print("4.Floor")
print("5.Cos(x)")
print("6.Sin(x)")
print("7.Tan(x)")
print("8.Fabs")
a=int(input("Enter you choise(1),(2)...:"))
if(a==1):
    r=int(input("Enter a nnumber:"))
    print(sqrt(r))
elif(a==2):
    x = int(input("Enter the base number: "))
    y = int(input("Enter the exponent: "))
    print(pow(x, y))
elif(a==3):
    x = float(input("Enter a number: "))
    print(ceil(x))
elif(a==4):
    x = float(input("Enter a number: "))
    print(floor(x))
elif(a==5):
    x = float(input("Enter an angle in radians: "))
    print(cos(x))
elif(a==6):
    x = float(input("Enter an angle in radians: "))
    print(sin(x))
elif(a==7):
    x = float(input("Enter an angle in radians: "))
    print(tan(x))
elif(a==8):
    x = float(input("Enter a number: "))
    print(fabs(x))
else:
    print("Invalid choice")
    x=int(input)