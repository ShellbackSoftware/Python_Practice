# Hangman game using the command line
import random
import string
word_list = ["Awkward", "Bagpipes", "Banjo", "Bungler", "Croquet", "Crypt", "Dwarves", "Fiery", "Fishhook", "Fjord", 
            "Gazebo", "Gypsy", "Haiku", "Haphazard", "Hyphen", "Ivory", "Jazzy", "Jiffy", "Jinx", "Jukebox", "Kayak",
            "Oxygen", "Pajama", "Phlegm", "Polka", "Quad", "Quip", "Sarcastic", "Rhythmic", "Zealous", "Wildebeast"]

# Default 6 wrong guesses - Head, torso, arms, legs
max_wrong_guesses = 6

# Pulls a random word from the word list
def get_word():
    return(word_list[random.randint(0,len(word_list))].lower())

# Gets a letter from user
def get_letter(guesses):
    while True:
        guess = raw_input("What is your guess? ").strip().lower()
        if len(guess) == 1 and guess in string.letters:
            if guess in guesses:
                print("You've already guessed {}, try again! ".format(guess))
                continue
            else:
                break
        else:
            print("Try again, but this time with ONE letter.")
            continue
    return guess

# Checks if user has exhausted wrong answers
def has_guesses(num):
    if num <= max_wrong_guesses:
        return True
    else:
        return False

# Checks if word has been guessed
def guessed_word(word, guesses):
    return set(word) <= set(guesses)

# Asks if user wants to play another game
def play_again(prompt):
    while True:
        value = raw_input(prompt).strip().lower()
        if value == "yes" or value == "y" or value == "no" or value == "n":
            break
        else:
            print("This is a yes or no question. Try again!")
            continue
    if value == "yes" or value == "y":
        return True
    return False

def printWord(word, guesses):
    result = ''
    for char in word:
        if char in guesses:
            result += ' {} '.format(char)
        else: 
            result += '_ '
    print(result)

def start_game():
    numGuesses = 0
    guesses = []
    current_word = get_word()
    while True:
        printWord(current_word, guesses)
        if has_guesses(numGuesses):
            current_guess = get_letter(guesses)
            guesses.append(current_guess)
            if current_guess in current_word:
                print(current_guess)
            else:
                if numGuesses < max_wrong_guesses:
                    print("Wrong! You have {} guesses remaining.".format(max_wrong_guesses-numGuesses))
                numGuesses += 1
            print("You have guessed {} so far. \n". format(guesses) )
            if guessed_word(current_word, guesses):
                again = play_again("Congratulations, you guessed '{}' correctly! Would you like to play again? ".format(current_word.capitalize()))
                if again:
                    numGuesses = 0
                    guesses = []
                    current_word = get_word()
                else:
                    break
        else: # Out of guesses
            again = play_again("Out of guesses! The word was {}. Would you like to play again? ".format(current_word.capitalize()))
            if again:
                numGuesses = 0
                guesses = []
                current_word = get_word()
            else:
                break

start_game()