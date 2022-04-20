import random

def play_guess_the_number():
    minimum = int(input("Please enter the minimum value: "))
    maximum = int(input("Please enter the maximum value: "))
    
    x = random.randrange(minimum, maximum)
    print(f"I am thinking of a number between {minimum} and {maximum}. Can you guess what it is?")
    
    while True:
        guess = int(input("Have a guess: "))
        if guess < x:
            print("Your guess is too low.")
        elif guess > x:
            print("Your guess is too high.")
        else:
            break
        print("Try again! ")
    print("Congratulations! You guessed my number!")
