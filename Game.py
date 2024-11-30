import random

def number_guessing_game():
    # Computer randomly chooses a number between 1 and 20
    number_to_guess = random.randint(1, 20)
    # Number of attempts allowed
    attempts = 3
    #Welcome messages
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        guess = int(input('Enter your guess: '))

        #input validation
        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
            continue

        #Providing Hints
        if guess < number_to_guess:
            print("Higher")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print("Congratulations! You have guessed the correct number!")
            return

        #Decrementing Attempts
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    #Game Over
    print(f"Sorry, you have run out of attempts. The number was {number_to_guess}.")


number_guessing_game()
