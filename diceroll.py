# Write code below 💖

import random

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"You rolled a {die1} and a {die2}. Total: {total}")

    if total == 2:
        print("Snake eyes!")
        break
    else:
        print("Not snake eyes. Rolling again.\n")
