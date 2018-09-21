import random

def Guess():
    randNumber = random.randint(1, 5)
    guess = int(input("Guess the number that random will generate: "))

    while (guess != randNumber):
        guess = int(input("Incorrect! Enter your next guess: "))

    print("Congratulations! You guessed the number correctly.")

while True:
    Guess()
