import random

while True:
    print("Guess the number that random will generate.")
    randNumber = random.randint(1, 5)

    if (int(input()) == randNumber):
        print("You guessed right!")
        break

    print("You guessed wrong, try again. The correct answer was " + str(randNumber) + ".")
