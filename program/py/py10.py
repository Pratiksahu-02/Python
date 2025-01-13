#WAP that will print the odd numbers from n1 to n2
#where the value of n1 and n2 are enter by user.
n1 = int(input("Enter the starting number (n1): "))
n2 = int(input("Enter the ending number (n2): "))

print(f"Odd numbers between {n1} and {n2} are:")
for num in range(n1, n2 + 1):
    if num % 2 != 0:
        print(num)