import random
import hangman_art
import hangman_words

print(hangman_art.logo)

random_word = random.choice(hangman_words.word_list)
# print(random_word)

placeholder = ""
for i in range(0, len(random_word)):
    placeholder += "_"

print(placeholder)

# print(guess)
# position = random_word.find(guess)
# print(position)

game_over = False
correct_letters = []
lives = 6

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    modified_placeholder = ""   

    for i in random_word:
        if i == guess:
            modified_placeholder += i
            correct_letters.append(guess)
        elif i in correct_letters:
            modified_placeholder += i   
        else:
            modified_placeholder += "_"
                
    print(modified_placeholder)

    if guess not in correct_letters:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(random_word)

    if "_" not in modified_placeholder:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])

    