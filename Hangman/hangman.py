from random import choice
import string
from graphics import hangmanpics, hangmanpics1


def get_word_list():
    words = []
    with open("words.txt") as f:
        for word in f:
            words.append(word.strip())
        return words


def print_word(word, guessed_letters, number_of_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
            number_of_letters -= 1
        else:
            print("_", end=" ")
    return number_of_letters


def get_guess(guessed_letters, all_letters):
    while True:
        guess = input("Please guess a letter:\n").upper()
        if guess in guessed_letters:
            print("You have already guessed this letter. Guess again")
        elif len(guess) > 1:
            print("Please only enter 1 letter at time. Guess again")
        elif guess == "":
            print("Please make an entry. Guess again")
        elif guess not in all_letters:
            print("Pease enter only letters, not numbers or characters. Guess again")
        else:
            return guess


def hangman():
    guesses_left = 7
    words = get_word_list()
    word = choice(words).upper()
    all_letters = list(string.ascii_uppercase)  # Uppercase alphabet
    guessed_letters = []
    number_of_letters = len(word)
    word = list(word)
    while guesses_left > 0 and number_of_letters > 0:
        number_of_letters = len(word)
        print(hangmanpics1[7 - guesses_left])
        print("You have", guesses_left, "guesses left")
        number_of_letters = print_word(word, guessed_letters, number_of_letters)
        print("\n\n")
        guess = get_guess(guessed_letters, all_letters)
        guessed_letters.append(guess)
        if guess not in word:
            guesses_left -= 1
        else:
            number_of_letters -= 1
    if guesses_left == 0:
        print(hangmanpics1[7])
        print("You Lost\nYou have been hung and have died\nThe word was", end=" ")
        for letter in word:
            print(letter, end="")
    elif number_of_letters == 0:
        print_word(word, guessed_letters, number_of_letters)
        print("\n")
        print("Congratulations, you have won")


if __name__ == "__main__":
    hangman()
