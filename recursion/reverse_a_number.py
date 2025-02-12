a=int(input("Enter a number:"))
rev=0
s=a 
while a>0: 
    rem=a%10
    rev=rev*10+rem
    a=a//10
if(rev==s):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")