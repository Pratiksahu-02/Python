from random import *
from time import sleep

def hangman():
    print("Welcome to Hangman!")
    sleep(1)
    print("I'm thinking of a word...")
    sleep(1)
    print("Can you guess what it is?")
    sleep(1)
    print("Here's a hint: It's a fruit.")
    sleep(1)
    print("You have 6 chances to guess the word.")
    sleep(1)
    print("Good luck!")
    sleep(1)
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    word=choice(words)
    word_list = list(word)
    l=[]
    for i in range(len(word)):
        l.append(word[i])
    letter1=choice(l)
    guess_list = []
    for letter in word_list:
        if letter == letter1:
            print(letter, end=" ")
            guess_list.append(letter)
        else:
            print("_", end=" ")
            guess_list.append("_")
    chances = 6
    while chances > 0:
        guess = input("\nGuess a letter: ")
        if guess in word_list:
            print("Correct!")
            for i in range(len(word_list)):
                if word_list[i] == guess:
                    guess_list[i] = guess
            print(" ".join(guess_list))
            if guess_list == word_list:
                print("Congratulations! You've guessed the word!")
                break
        else:
            chances -= 1
            print("Incorrect! You have", chances, "chances left.")
    if chances == 0:
        print("Game over! The word was", word)
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing Hangman!")
        sleep(1)
        print("Goodbye!")
        sleep(1)

hangman()