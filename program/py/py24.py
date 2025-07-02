#Write a program that will find x^n (x to the power of n) using a function. 
#The function receives the value of x, n and should return the value of x^n. 
#[don’t use any mathematical function].

def power(x,n):
    a=x**n
    return a

x=int(input("Enter the base(x) of the number:"))
n=int(input("Enter the power(n) of the number:"))
print("The solution(x^n) is:",power(x,n))
