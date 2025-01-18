def fibonacci(u):
    if u <= 0:
        return 0
    elif u == 1:
        return 1
    else:
        return fibonacci(u-1) + fibonacci(u-2)


n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i))

# Example: fibonacci(6) should return 8
