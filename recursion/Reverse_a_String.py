def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]


s=input("Enter the string: ")
print(reverse_string(s))
# Example: reverse_string("hello") should return "olleh"
