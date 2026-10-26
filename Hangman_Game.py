import random

# List of words
words = ["python", "computer", "keyboard", "program", "internet"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

print("Guess the hidden word!")
print("You have 6 wrong attempts.")

while wrong_attempts < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts left:", max_attempts - wrong_attempts)

    # Check if player won
    if "_" not in display_word:
        print("\nCongratulations! You won!")
        print("The word was:", secret_word)
        break

    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

else:
    print("\nGame Over! You lost!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
