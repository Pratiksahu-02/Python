def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)


n=int(input("Enter a number: "))
print(sum_of_digits(n))
# Example: sum_of_digits(1234) should return 10
