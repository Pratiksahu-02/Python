def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)




a=int(input("Enter a number:"))
print("Factorial of num is:",factorial(a))
# Example: factorial(5) should return 120
