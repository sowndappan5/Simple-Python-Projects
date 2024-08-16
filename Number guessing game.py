import math
import random

# User Inputs
lower = int(input("Enter Lower range:- "))
upper = int(input("Enter Upper range:- "))

# generating random numbers between the lower and upper
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the number!\n")

# Initializing the number of guesses
count = 0
flag = False

while count < total_chances:
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition matching
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,shows this output.
if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")