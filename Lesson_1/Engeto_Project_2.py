import random
import time
from datetime import datetime

def generate_secret_number():
    """
    Generate a random 4-digit number where:
    - The first digit is between 1 and 9 (not 0).
    - All digits are unique.
    Returns:
        str: A string representation of the 4-digit number.
    """
    digits = list(range(1, 10))
    random.shuffle(digits)
    return str(digits[0]) + ''.join(str(x) for x in random.sample(range(0, 10), 3) if x != digits[0])

def validate_guess(guess):
    """
    Validate the user's guess.
    Checks:
    - The guess is exactly 4 digits long.
    - The guess does not start with 0.
    - The guess contains only digits.
    - All digits in the guess are unique.
    Args:
        guess (str): The user's input guess.
    Returns:
        str: An error message if the input is invalid, otherwise an empty string.
    """
    if len(guess) != 4:
        return "Invalid input: Enter a 4-digit number."
    if guess[0] == '0':
        return "Invalid input: The number should not start with 0."
    if not guess.isdigit():
        return "Invalid input: Enter only digits."
    if len(set(guess)) != 4:
        return "Invalid input: Each digit must be unique."
    return ""

def evaluate_guess(secret, guess):
    """
    Evaluate the user's guess against the secret number.
    Calculates the number of bulls (correct digits in the correct position)
    and cows (correct digits in the wrong position).
    Args:
        secret (str): The secret 4-digit number.
        guess (str): The user's guessed 4-digit number.
    Returns:
        tuple: A tuple containing the counts of bulls and cows.
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def save_statistics(guesses, time_taken):
    """
    Save the game statistics to a file.
    Logs the date, number of guesses, and total time taken.
    Args:
        guesses (int): The total number of guesses made by the user.
        time_taken (float): The total time taken in seconds.
    """
    with open("game_statistics.txt", "a") as file:
        file.write(f"Date: {datetime.now()}, Guesses: {guesses}, Time: {time_taken:.2f} seconds\n")

def get_best_time():
    """
    Retrieve the fastest game time from the statistics file.
    Returns:
        float: The fastest time in seconds, or None if no records exist.
    """
    try:
        with open("game_statistics.txt", "r") as file:
            times = [float(line.split("Time: ")[1].split(" seconds")[0]) for line in file if "Time:" in line]
        return min(times) if times else None
    except FileNotFoundError:
        return None

def play_game():
    """
    Function to handle the core game loop.
    Manages secret number generation, user guesses, and game completion.
    """
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number: ")
        validation_message = validate_guess(guess)
        if validation_message:
            print(validation_message)
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"It took you {int(time_taken // 60)} minutes and {int(time_taken % 60)} seconds.")

            # Získání nejlepšího času před uložením aktuálního
            best_time = get_best_time()

            # Porovnání aktuálního času s nejlepším
            if best_time is None or time_taken < best_time:
                print("Congratulations! This is your fastest game time!")
            else:
                print(f"Your time was {int(time_taken // 60)} minutes and {int(time_taken % 60)} seconds.")
                print(f"The fastest game time so far is {int(best_time // 60)} minutes and {int(best_time % 60)} seconds.")

            save_statistics(attempts, time_taken)
            return
        else:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")


def ask_to_play_again():
    """
    Prompt the user to decide whether they want to play again.
    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response in ('yes', 'y'):
            return True
        elif response in ('no', 'n'):
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def print_game_intro():
    """
    Print the introduction and rules of the game, along with the fastest game time if available.
    """
    print("Hi there!")
    print("-" * 55)
    best_time = get_best_time()
    if best_time:
        print(f"Fastest game so far: {int(best_time // 60)} minutes and {int(best_time % 60)} seconds.")
    else:
        print("No fastest time recorded yet. Be the first!")
    print("-" * 55)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("Rules:")
    print("1) You can choose from numbers between 0 - 9.")
    print("2) Each number occurs only once.")
    print("3) Bull - correct number in the correct position.")
    print("   Cow - correct number in the wrong position.")
    print("-" * 55)

def main():
    """
    Main function to play the Bulls and Cows game.
    Handles the game flow and replay logic.
    """
    print_game_intro()
    while True:
        play_game()
        if not ask_to_play_again():
            print("Goodbye for now!")
            break

if __name__ == "__main__":
    main()
