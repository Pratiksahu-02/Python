from random import *
from time import sleep

def yes():
    while True:
        answer=input("Would you like to play again? (y/n): ")
        if answer=="y":
            rock_paper_scissors()
        elif answer=="n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please try again.")
            yes()

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    t=int(input("How many rounds would you like to play?: "))
    print("You will be playing",t,"rounds.")
    print("The game will begin in 3 seconds.")
    sleep(3)
    print("Rock...")
    sleep(1)
    print("Paper...")
    sleep(1)
    print("Scissors...")
    sleep(1)
    print("Shoot!")
    print()
    user_score=0
    computer_score=0
    for i in range(t):
        print("Round",i+1)
        user=input("Rock, Paper, or Scissors?: ")
        computer=randint(1,3)
        if computer==1:
            computer="Rock"
        elif computer==2:
            computer="Paper"
        else:
            computer="Scissors"
        print("Computer:",computer)
        if user=="Rock" and computer=="Scissors":
            print("You win!")
            user_score+=1
        elif user=="Rock" and computer=="Paper":
            print("You lose!")
            computer_score+=1
        elif user=="Paper" and computer=="Rock":
            print("You win!")
            user_score+=1
        elif user=="Paper" and computer=="Scissors":
            print("You lose!")
            computer_score+=1
        elif user=="Scissors" and computer=="Paper":
            print("You win!")
            user_score+=1
        elif user=="Scissors" and computer=="Rock":
            print("You lose!")
            computer_score+=1
        else:
            print("It's a tie!")
        print()
    print("Game Over!")
    if user_score>computer_score:
        print("You win the game!")
    elif user_score<computer_score:
        print("You lose the game!")
    else:
        print("The game is a tie!")
    print("Your score:",user_score)
    print("Computer's score:",computer_score)
    yes()

rock_paper_scissors()