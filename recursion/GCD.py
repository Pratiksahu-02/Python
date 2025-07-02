def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(f"GCD of {a} and {b} is {gcd(a, b)}")
# Example: gcd(48, 18) should return 6
