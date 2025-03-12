from time import sleep
from random import *

print("Welcome to the question generator.")
sleep(1)
print("This program will generate questions based on the topics of mathematics.")
sleep(1)
print("Question Generation has start in")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)

def que_gen(a):
    list=["addition","subtraction","multiplication","division","square","cube","square root","cube root","percentage","average","LCM","HCF","simple interest","compound interest"]
    #,"profit and loss","time and work","time and distance","area and perimeter","volume and surface area","probability","permutation and combination","algebra","geometry","trigonometry","mensuration","statistics","data interpretation","data sufficiency","reasoning","puzzle","blood relation","coding and decoding","series","clock","calendar","direction","syllogism","seating arrangement","input output","statement and argument","statement and assumption","statement and conclusion","course of action","cause and effect","inference","decision making","data sufficiency","data interpretation","data analysis"
    for i in range(a):
        x=choice(list)
        if x=="addition":
            print("What is the sum of",randint(1,100),"and",randint(1,100),"?")
        elif x=="subtraction":
            print("What is the difference between",randint(1,100),"and",randint(1,100),"?")
        elif x=="multiplication":
            print("What is the product of",randint(1,100),"and",randint(1,100),"?")
        elif x=="division":
            print("What is the quotient when",randint(1,100),"is divided by",randint(1,100),"?")
        elif x=="square":
            print("What is the square of",randint(1,100),"?")
        elif x=="cube":
            print("What is the cube of",randint(1,100),"?")
        elif x=="square root":
            print("What is the square root of",randint(1,100),"?")
        elif x=="cube root":
            print("What is the cube root of",randint(1,100),"?")
        elif x=="percentage":
            print("What is",randint(1,100),"percent of",randint(1,100),"?")
        elif x=="average":
            print("What is the average of",randint(1,100),",",randint(1,100),"and",randint(1,100),"?")
        elif x=="LCM":
            print("What is the LCM of",randint(1,100),"and",randint(1,100),"?")
        elif x=="HCF":
            print("What is the HCF of",randint(1,100),"and",randint(1,100),"?")
        elif x=="simple interest":
            print("What is the simple interest on",randint(1,100),"at",randint(1,100),"percent for",randint(1,100),"years?")
        elif x=="compound interest":
            print("What is the compound interest on",randint(1,100),"at",randint(1,100),"percent for",randint(1,100),"years?")
        sleep(1)
    yes()
    
def yes():
    print("Do you want to generate more questions?")
    x=input("Enter 'y' for yes and 'n' for no: ")
    if x=="y":
        n=int(input("Enter the number of questions you want to generate: "))
        que_gen(n)
    else:
        print("Thank you for using the question generator.")

n=int(input("Enter the number of questions you want to generate: ")) 
que_gen(n)