def yes():
    print("Do you want to continue(y/n):")
    c=input()
    if(c=='y'):
        fun()
    elif(c=='n'):
        print("Thank you")
    else:
        print("Invalid choice")
        yes()

def add():
    n=int(input("enter how many number u want to add:"))
    sum=0
    for i in range(n):
        a=int(input("enter a number:"))
        sum=sum+a
    print("sum of numbers is:",sum)
    yes()


def sub():
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    sub=0
    sub=x-y
    print("sub of numbers is:",sub)
    yes()

def multi():
    n=int(input("enter how many number u want to multi:"))
    multi=1
    for i in range(n):
        a=int(input("enter a number:"))
        multi=multi*a
    print("multi of numbers is:",multi)
    yes()

def devision():
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    dev=x/y
    print("devision of numbers is:",dev)
    yes()

def floot_devision():
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    floot_dev=x//y
    print("floot devision of numbers is:",floot_dev)
    yes()

def power():
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    power=x**y
    print("power of numbers is:",power)
    yes()


def fun():
    c=int(input("Enter a number(1-6):"))
    if(c==1):
        add()
    elif(c==2):
        sub()
    elif(c==3):
        multi()
    elif(c==4):
        devision()
    elif(c==5):
        floot_devision()
    elif(c==6):
        power()
    else:
        print("Invalid choice")
        fun()

def main():
    print("choice:")
    print("1.Add")
    print("2.sub")
    print("3.multi")
    print("4.devision")
    print("5.floot devision")
    print("6.power")
 
if __name__=='__main__':
    main()
    fun()