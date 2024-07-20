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

teminate_program()

guess = str(input("Guess the word : ")).strip()
num = []
count = 0
num.append(guess)
count = len(num)
print (num)
print(count)