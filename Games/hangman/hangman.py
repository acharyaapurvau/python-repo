import random
import hangmanstages
import hangmanWords
lives = 6

word = random.choice(hangmanWords.words_list)
print("Welcome to Hangman!")
placeholder = "_" * len(word)
print("Word to guess: " + " ".join(placeholder))

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.\n")
        continue

    guessed_letters.append(guess)
    display = ""

    for letter in word:
        if letter == guess or letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Add guessed letter to correct_letters if correct
    if guess in word and guess not in correct_letters:
        correct_letters.append(guess)

    print("\n" + " ".join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    if guess not in word:
        lives -= 1
        print(hangmanstages.stages[6-lives])
        print(f"You have {lives} lives left. ")
        if lives == 0:
            game_over = True
            print(f"You lose! The word was '{word}'.")

    if "_" not in display:
        game_over = True
        print("Congratulations! You win!")
