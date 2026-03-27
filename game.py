import random
secret_number = random.randint(1, 20)
guesses = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    guesses += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {guesses} tries.")
        break 