import random

word_list = ["vibe", "flux", "glow", "myth", "fams"]

secret_word = random.choice(word_list)

guessed_letters = []      
incorrect_guesses = 0    
max_guesses = 6           

print("\t-------🎮 Welcome to Hangman!-------")
print("Guess the word one letter at a time.")
print(f"You have {max_guesses} incorrect guesses.\n")

while True:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("Word:", " ".join(display))

    if "_" not in display:
        print("\n🎉 You won! The word was:", secret_word)
        break

    if incorrect_guesses >= max_guesses:
        print("\n💀 You lost! The word was:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.\n")
        continue
    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! {max_guesses - incorrect_guesses} tries left.\n")
