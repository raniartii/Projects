import random
import time
import sys
def teminate_program():
    print('----------------------------')
    time.sleep(0.5)
    print('----------------------------')
    time.sleep(0.5)
    print('Exiting')
    time.sleep(0.5)
    print('............................')
    time.sleep(0.5)
    print('............................')
    time.sleep(0.5)
    print('Program terminated')  
    sys.exit(0)

hints = ['a programming language & a snake', 'king of veggies', 'king of fruits']
words = ['python', 'aaloo', 'mango']

play_more = True

while play_more:
    index = random.randint(0, len(hints) - 1)
    guesses =  0
    num = []
    while True:
        print(hints[index])
        guess = input("Guess the word: ").strip().lower()
        if guess == words[index]:
            print("\nCorrect!")
            response = input("Do you want to play more? (yes/no): \n").strip().lower()
            if response == 'yes':
                play_more = True
            else:
                # from test import terminate_program
                teminate_program()
            break
        else:
            guesses = guesses+1
            num.append(guess)
            print('Words you guessed: ', num)
            print(guesses, 'Incorrect guesses\n')
            print("Incorrect. Try again!")
    