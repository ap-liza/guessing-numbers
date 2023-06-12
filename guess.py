import random

def guessNumber(x):
    random_number= random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess > random_number:
            print("Oops too high, try again")
        elif guess < random_number:
            print("Oops too low, try again")
        else:
            print(f"Yayyy Congrats!!! You have guessed the number {random_number} correctly")
            
guessNumber(110)
