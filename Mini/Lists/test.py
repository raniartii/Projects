'''ans = [['a','a','m'],['i','n','k'],['t','a','a'],['p','e','a'],['m','o','m'],['y','u','m']]
# for el in range (len(ans)):
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

leng = len(ans)
print(leng)
print(ans)
print(ans[0])
print(ans[1])
print(ans[2])

string = "GFG"
ch_iterator = iter(string)
 
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))

for i in string:
    ch = iter(string)
    print(ch_iterator, ':ye for loop wala hai')

# Create a 3D list with dimensions 3x3x3
three_d_list = [[[0 for col in range(3)] for col in range(3)] for row in range(3)]
print(three_d_list)'''


l1 = []
import random
words2 = l1[::]
random.shuffle(words2)
for w in words2:
    print(f'the hin is : {w}')
    ans = str(input('enter the answer : '))
    for a in l1:
        if ans == a:
            print('correct')
        else: 
            print('guess again')

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

'''guess = str(input("Guess the word : ")).strip()
num = []
count = 0
num.append(guess)
count = len(num)
print (num)
print(count)'''

import random

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
                teminate_program()
            break
        else:
            guesses = guesses+1
            num.append(guess)
            print('Words you guessed: ', num)
            print(guesses, 'Incorrect guesses\n')
            print("Incorrect. Try again!")
            
