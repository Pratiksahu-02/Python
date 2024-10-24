#WAP that will convert various temperatures.
#a.Fahrenheit to Centigrate
#b.Centigrate to Fahrenheit
print("Choice what you want to convert")
print("1.Fahrenheit to Centigrate")
print("2.Centigrate to Fahrenheit")
a=int(input("Enter your choice(1)(2):"))
if(a==1):
    f=int(input("Enter Faharnheit:"))
    c=(f-32)*(5/9)
    print("Centigrate =",c)
else:
    c=int(input("Enter Centigrate:"))
    f=(c*(9/5))+32
    print("Faharnheit =",f)