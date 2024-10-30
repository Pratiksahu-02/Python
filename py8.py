# Find out the youngest among Shyam, Dugu and Ishan whose ages are entered by the user through keyboard.
Shyam=10 #int(input("Enter your age:"))
Dugu=12 #int(input("Enter your age:"))
Ishan=14 #int(input("Enter your age:"))
if(Shyam<Dugu):
    if(Shyam<Ishan):
        print("Shyam is younger.")
    else:
        print("Ishan is younger.")
else:
    if(Dugu<Ishan):
        print("Dugu is younger.")
    else:
        print("Ishan is younger.")