import sys
import time

def guess_works (guess, greens, yellows, greys):
    """Returns a boolean representing whether this guess would work with the users information"""

    # Make sure greens are present
    for i in range(0, len(greens)):
        if greens[i] != "-" and greens[i] != guess[i]:
            return False

    # Make sure there are no greys
    for grey in greys:
        if grey in guess:
            return False

    # Make sure yellows are present and in a possible position
    for yellow in yellows:
        if yellow not in guess:
            return False
        else:
            for i in range(0, len(yellows[yellow])):
                if yellows[yellow][i] == "x" and guess[i] == yellow:
                    return False

    return True

def main():
    # Get greens
    print("First you will enter the green letters you have")
    print("You will enter the green you have in each spot, else -")
    print("For example, if you have a T in the first position and a B in the third position, you will enter T-B--")
    greens = input("Enter your greens: ").lower()

    # Get yellows
    print("\nNow you will enter your yellows")
    print("You will enter the letters that are yellow in any order, without spaces")
    yellows = input("Enter your yellows: ").lower().replace(" ", "")
    yellows_dict = {}

    if len(yellows) > 0:
        # Narrow down yellows
        print("\nNow you will specify where you have already guessed your yellows")
        print("When prompted with a yellow, enter an X for each place that you have guessed it, else -")
        for letter in yellows:
            yellows_dict[letter] = input("  {}: ".format(letter.upper())).lower()

    # Get greys
    print("\nNow you will enter your greys")
    print("You will enter all of your grey letters in any order, without spaces")
    greys = input("Enter your greys: ").lower().replace(" ", "")

    user_options = []
    for guess in possible_guesses:
        if guess_works(guess, greens, yellows_dict, greys):
            user_options.append(guess)

    print("Your options:\n  ", end="")
    print(*user_options, sep="\n  ")

    again = input("\nGo again? (y/n) ").lower()
    if again == "y":
        print("\n")
        main()
    else:
        sys.exit()

# Load and sort guesses
with open("valid_guesses.txt") as valid_guesses:
    possible_guesses = valid_guesses.read().split("\n")
possible_guesses.sort()

print("\nWelcome to Wordle Solver!\n")
time.sleep(1)

if __name__ == "__main__":
    main()