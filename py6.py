# WAP that will ask you to enter your name through keyword , add perform following opration 
# a.find the middle name .
# b.find the last name with (using string slicing)
# c.Re-write the name with surname first.

a=input("Enter your name:")
b=a.split()

if(len(b)>2):
    print(b[1])

# Last Name:
print(a[-1: :])

print(b[-1],end=" ")
for i in range(len(b)-1):
    print(b[i],end=" ")