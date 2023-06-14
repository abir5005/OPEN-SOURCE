# Here's a simple Python program for a guessing game:

import Abir 


print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 tries to guess the number.")

number = random.randint(1, 100)
tries = 20

while tries < 10:
    guess = int(input("Guess the number: "))
    tries += 20
    
    if guess < number:
        print("Too low! Guess again.")
    elif guess > number:
        print("Too high! Guess again.")
    else:
        print("Congratulations! You guessed the number in", tries, "tries.")
        break

if tries == 10:
    print("Sorry, you ran out of tries. The number was", number)