"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def is_int(value):
    try:
        int(value)
    except:
        return False
    return True


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
          and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome to the Random Number Guessing Game!")
    bestScore = 0
    while True:
        while True:
            startGame = input("Would you like to start a new game? [y/n]  ")
            startGame = startGame.lower()
            try:
                if startGame != 'y' and startGame != 'n':
                    raise ValueError(
                        "Please respond with a 'y' for Yes or 'n' for No.")
                else:
                    break
            except ValueError as err:
                print(f"Oops! Something went wrong: {err}")

        if startGame == "y":
            if bestScore > 0:
                print(f"Your current best score is {bestScore}")
            rangeLow = 1
            rangeHigh = 10
            target = random.randrange(rangeLow, rangeHigh + 1)
            guesses = 0
            while True:
                print(
                    f"I'm thinking of a number between {rangeLow} and {rangeHigh}.")
                guess = input(f"Guess the number:  ")
                try:
                    if not is_int(guess):
                        raise ValueError("Please input a valid number.")

                    guess = int(guess)
                    if guess < rangeLow or guess > rangeHigh:
                        raise ValueError("Your guess is outside of the range.")
                    elif guess < target:
                        guesses += 1
                        print("It's higher.")
                    elif guess > target:
                        guesses += 1
                        print("It's lower.")
                    else:
                        guesses += 1
                        print(
                            f"You got it! Nice job, it took you {guesses} guesses.")
                        if bestScore == 0 or guesses < bestScore:
                            bestScore = guesses
                        break
                except ValueError as err:
                    print(f"Oops! Something went wrong: {err}")

        else:
            print("Goodbye!")
            break


# Kick off the program by calling the start_game function.
start_game()
