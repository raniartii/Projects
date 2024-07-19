import random

#Function to continue or end game

def play_more():
    ask = str(input('Do you want to play more? Yes/No : \n'))
    if ask.casefold() == 'yes':
        guess()
    else:
        from test import terminate_program
        terminate_program()

#Hints & Answers

hints = ['a programming language & a snake', 'king of veggies', 'king of fruits', 'mother\'s son-in-law\'s mother\'s grand daughter']
words = ['python', 'aaloo', 'mango', 'neice']

def welcome():
    print("Welcome to the puzzle world")

#Guess word & check function
    
def guess():
    global guesses
    play = True
    while play:
        index = random.randint(0, len(hints)-1)
        guesses = 0

        while True:
            def check():
                print(hints[index])
                guess = str(input("\nGuess the word : ")).strip()
                guess_list = []
                guess_list.append(guess)
                if guess.casefold() == words[index]:
                    print("\nCorrect!\n")
                    play_more() 
                else:
                    guesses = guesses+1
                    print("\nIncorrect. Try again!\n")
                    print('Number of incorrect guesses: ', guesses)
                    print('\nWords you guessed: ', guess_list, '\n')
                    check()
            check()

welcome()
guess()
# def execute():
#     for i in hints:
#         welcome()
#         guess()

# execute()