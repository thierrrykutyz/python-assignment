import random
import string

'''  Group members:

Ishimwe Boncoeur    -- Reg nø: 223015833

Kubwimaba Thierry   --Regnø: 223003944  '''

# List of English words for the game
word_list =["grapefruit", "kiwi", "blackberry", "apricot", "pear", "mango", "cranberry"]
# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to initialize the game
def initialize_game():
    secret_word = choose_word()
    guessed_letters = set()
    guesses_remaining = 6
    warnings_remaining = 3
    return secret_word, guessed_letters, guesses_remaining, warnings_remaining

# Function to display the current status of the game
def display_status(secret_word, guessed_letters):
    word_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_display += letter
        else:
            word_display += "-"
    return word_display

# Function to check if the game has been won
def is_game_won(secret_word, guessed_letters):
    return set(secret_word) == guessed_letters

# Function to play the Hangman game
def play_hangman():
    print("Welcome to Hangman!")
    secret_word, guessed_letters, guesses_remaining, warnings_remaining = initialize_game()

    while guesses_remaining > 0:
        print("You have {} guesses left.".format(guesses_remaining))
        print("Available letters:", "".join(sorted(set(string.ascii_lowercase) - guessed_letters)))
        print("Word:", display_status(secret_word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Invalid input. You have {} warnings left.".format(warnings_remaining))
            else:
                guesses_remaining -= 1
                print("Invalid input. No warnings left. You lose a guess.")
        elif guess in guessed_letters:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("You've already guessed that letter. You have {} warnings left.".format(warnings_remaining))
            else:
                guesses_remaining -= 1
                print("You've already guessed that letter. No warnings left. You lose a guess.")
        else:
            guessed_letters.add(guess)
            if guess in secret_word:
                print("Good guess!")
            else:
                if guess in "aeiou":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print("Oops! That letter is not in the word.")

        if is_game_won(secret_word, guessed_letters):
            score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you've won! Your score is:", score)
            break

    if guesses_remaining <= 0:
        print("Sorry, you've run out of guesses. The word was:", secret_word)

# Start the game
play_hangman()
