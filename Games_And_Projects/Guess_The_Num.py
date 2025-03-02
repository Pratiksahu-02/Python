from random import *

def yes():
    c=input("Do you want to continue(y/n):")
    if(c=='y'):
        guess()
    elif(c=='n'):
        print("Thank you")
    else:
        print("Invalid choice")
        yes()

def guess():
    n=randint(1,100)
    while True:
        a=int(input("Enter the number between 1 to 100:"))
        if(a<n):
            print("Enter a bigger number")
        elif(a>n):
            print("Enter a smaller number")
        else:
            print("You have guessed the number")
            break
    yes()   
guess()