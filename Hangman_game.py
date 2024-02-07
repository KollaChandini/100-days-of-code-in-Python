import random

import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)
#creating an empty list 
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
# if user entered a letter that he already guessed
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
#check if user is wrong
    if guess not in chosen_word:
        print(f"Guessed letter is {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game =True
        print("You won.")
    from hangman_art import stages
    print(stages[lives])

