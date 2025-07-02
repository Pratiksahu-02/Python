#Write a program to demonstrate stack and queue 
#operations using a list of numbers.

"""STACK IMPLEMENTATION
Stack:Implementation as a list 
top:integer having a position of top most element in stack"""


#isempty operation
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
#Push operation
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
#Pop operation
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return item
         
#Peek operation
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]

#isfully operation
def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-TOP")
        for i in range(top-1,-1,-1):
            print(stk[i])

#Main
stk=[]
top=None
while True:
    print("Stack Operation:")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display stack")
    print("5.Exit")
    c=int(input("Enter your choice(1-5):"))
    if c==1:
        item=int(input("Enter item:"))
        Push(stk,item)
    elif c==2:
        item=Pop(stk)
        if (item=="Underflow") :
            print("Underflow: Stack is empty.")
        else:
            print("Poped item is ",item)
    elif c==3:
        item=Peek(stk)
        if (item=="Underflow") :
            print("Underflow:Stack is empty.")
        else:
            print("Top most  item is ",item)
    elif c==4:
        Display(stk)
    elif c==5:
        break
    else:
        print("Invalid Choice")