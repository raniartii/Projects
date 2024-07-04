import time
import os
import sys
import functools
def addition():
    num = list(map(float, input("Enter the numbers to be added, seperated by 1 space: ").split()))
    a = sum(num)
    print("Sum of the numbers you entered is: ", a)
    operation()
    time.sleep(10)
    os.system('cls')

def differrence():
    num = list(map(float, input("Enter the numbers to be subtracted, seperated by 1 space: ").split()))
    diff = functools.reduce(lambda a,b: a-b, num)
    print("Difference of the numbers you entered is: ", diff)
    operation()
    time.sleep(10)

def division():
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    if divisor == 0: 
        print("Division error: Cannot divide by zero")
    elif dividend == 0:
        print(0)
    else:
        div = dividend / divisor
        mod = dividend % divisor
        print(f'Quotient of {dividend} and {divisor} is: {div}')
        print(f'Remainder of {dividend} and {divisor} is: {mod}')
    operation()
    time.sleep(10)
    
def multiplication():
    num = list(map(float, input("Enter the numbers to be multiplied, seperated by 1 space: ").split()))
    mult = 1
    for i in num:
        mult = mult * i
    print(mult)
    operation()
    time.sleep(10)

def power():
    b = float(input("Enter the base value: "))
    e = int(input("Enter the exponent: "))
    x = pow(b ,e)
    print(x)
    operation()
    time.sleep(10)

def square():
    s = float(input("Enter the number: "))
    sq = s ** 2
    print(sq)
    operation()
    time.sleep(10)

def factorial():
    fact = 1
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial can't be calculated.")
    for i in range(1, n+1):
        fact = fact*i
    print(fact)
    operation()
    time.sleep(10)
    
def exit():
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

def operation():
    print(
        '''********Welcome to kallu's kalculatorr********
       ====User Menu for Operations====

                1. Addition
                2. Difference
                3. Division
                4. Multiplication
                5. Power
                6. Square
                7. Factorial
                8. Exit
        '''
    )
    
    choice = int(input("Please select operation number to be performed: "))
    if choice == 1:
        addition()
        os.system('cls')
    elif choice == 2:
        differrence()
        os.system('cls')
    elif choice == 3:
        division()
        os.system('cls')
    elif choice == 4:
        multiplication()
        os.system('cls')
    elif choice == 5:
        power()
        os.system('cls')
    elif choice == 6:
        square()
        os.system('cls')
    elif choice == 7:
        factorial()
        os.system('cls')
    elif choice == 8:
        exit()
        os.system('cls')
    elif choice>7:
        print("please enter a valid operation")
        operation()
        os.system('cls')
    else:
        os.system('cls')
        return 0
operation()