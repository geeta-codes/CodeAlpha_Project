import random

#List of predefined words 
words = ["sonali","tiger","python","house","flower"]

#selection of random word
word = random.choice(words)

#create blanks
guessed_word = ["_"]*len(word)

guessed_letters=[]
attempts = 6

print("===== WELCOME TO HANGMAN GAME =====")

while attempts>0 and "_" in guessed_word:
    print("\n Word:","".join(guessed_word))
    print("Guessed Letters:","".join(guessed_letters))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter:").lower()

    # Check valid input 
    if len(guess) != 1 or not guess.isalpha():
     print("Please enter only one alphabet.")
     continue

    # Check if already guessed 
    if guess in guessed_letters:
     print("You already guessed that letter.")
     continue 

    guessed_letters.append(guess)

    # Check if already is correct 
    if guess in word:
     for i in range(len(word)):
        if word[i] == guess:
            guessed_word[i] = guess
     print("CORRECT!")
    else:
     attempts -= 1
     print("WRONG GUESS!")
# Game result
if "_"  not in guessed_word:
    print ("\n CONGRATULATIONS! You guessed the word :" , word)
else:
    print("\n GAME OVER!")
    print ("The correct word was:",word)