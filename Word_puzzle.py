# Creative Addition:
# This version keeps track of all previous guesses and displays them at the end
# so the player can review their progress.

print("Welcome to the word guessing game!\n")

secret_word = "mosiah"
secret_word = secret_word.lower()
word_length = len(secret_word)

hint = "_ " * word_length
print("Your hint is:", hint)

guess_count = 0
previous_guesses = []

guess = input("What is your guess? ").lower()
guess_count += 1
previous_guesses.append(guess)

while guess != secret_word:
    if len(guess) != word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
    else:
        hint_result = ""

        for i in range(word_length):
            if guess[i] == secret_word[i]:
                hint_result += guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint_result += guess[i].lower() + " "
            else:
                hint_result += "_ "

        print("Your hint is:", hint_result)

    guess = input("What is your guess? ").lower()
    guess_count += 1
    previous_guesses.append(guess)

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.\n")

print("Your previous guesses were:")
for g in previous_guesses:
    print(" -", g)