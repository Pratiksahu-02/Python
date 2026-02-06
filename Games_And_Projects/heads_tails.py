import random

while True:
    result = random.choice(["Heads", "Tails"])
    print("🪙 Coin landed on:", result)

    again = input("Toss again? (y/n): ")
    if again.lower() != "y":
        break
print("Thanks for playing!")
