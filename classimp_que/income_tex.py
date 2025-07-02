income=float(input("Enter your income:"))
if(income<=250000):
    print("no tax")
elif(income>250000 and income<=500000):
    print("You need to give 5% tax",(income-250000)*(5/100))
elif(income>500000 and income<=1000000):
    print("You need to give 20% tax",(250000*0.05)+(income-500000)*(20/100))
elif(income>1000000):
    print("You need to give 30% tax",(250000*0.05)+(500000*0.20)+(income-1000000)*(30/100))