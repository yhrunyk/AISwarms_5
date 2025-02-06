import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
