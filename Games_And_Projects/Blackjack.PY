from random import *
from time import sleep

def yes():
    n=input("Do you want to play again? (y/n)")
    if n=="y":
        blackjack()
    else:
        print("Thanks for playing!")
        sleep(1)
        exit()

def blackjack():
    yes()

blackjack()