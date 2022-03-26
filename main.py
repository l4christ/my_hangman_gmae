import random
from hangman_art import stages, logo
from hangman_words import word_list

#display the ascii art for the hangman
print(logo)
game_is_finished = False
lives = len(stages) - 1

#select a random item from the list
chosen_word = random.choice(word_list)

#get the length of the selected item
word_length = len(chosen_word)

#create an empty list to display the dashes

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

   
    #check if the guessed word is in display list
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        
        #get the position of each letter in the chosen item
        
        letter = chosen_word[position]
        #if the letter entered by the user is equal to any letter in the chosen word, then put the letter in same position in the display list
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
