import random

words = ['caleb', 'daniel', 'watermelon', 'warriors', 'thunder', 'kilimanjaro', 'lebron', 'xlyophone', 'complicated', 'lucas']
random_word = random.choice(words)
words_len = len(words)
guess = ""
count = 7
enter = ""
temp = "_ " * words_len
guess_list = []


print(""" Welocme to our word guessing game. 
The objective is to guess the word before you run out of guesses.
You have 7 guesses to attempt to guess the word correctly. 
Good luck!""")


# to print the number of underscores the letter has 

print(temp)

game_over = False
#This should repeat the guess letter function
while True:
    guess = str(input("Guess a letter:  ")).lower()

# checks to see if the letter is in the word
    if guess not in guess_list: 

        i = 0
        if guess in random_word:
            
            while random_word.find(guess, i) != -1:
                i = random_word.find(guess, i)
                temp = temp[:i] + guess + temp[i + 1:]
                i += 1
            print("Congrats, it's in the word.")
            

            print(temp)

        else: 
            count -= 1
            print("Sorry your letter is not in the word, attempts left: ", count)

        if count == 0:
                print("Sorry, you have reached the max attempts, Game Over.")
                game_over=True
        if words == temp: 
            print("Congrats, you have won the game. The word was " + random_word)
            game_over = True

    else: 

        print("You have already guessed this letter, Try another letter".format(guess))
        print(set(guess_list))
