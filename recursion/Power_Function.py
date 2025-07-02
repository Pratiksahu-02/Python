def power(n,i):
    if i==0:
        return 1
    else:
        return n*power(n,i-1)
    
n=int(input("Enter the number: "))
i=int(input("Enter the power: "))
print(f"Power of {n}^{i} is {power(n,i)}")

# Example: power(2, 3) should return 8