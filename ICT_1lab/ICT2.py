import random

target = random.randint(1, 100)
print("Guess the number between 1 and 100 (or type 'q' to quit).")

while True:
    guess = input("Enter your guess: ").strip()
    
    if guess.lower() == 'q':
        print("Exiting the game. Goodbye!")
        break
    
    try:
        guess = int(guess)
        if guess > target:
            print("Too high!")
        elif guess < target:
            print("Too low!")
        else:
            print("Congratulations! You guessed the correct number!")
            break
    except ValueError:
        print("Please enter a valid number.")
