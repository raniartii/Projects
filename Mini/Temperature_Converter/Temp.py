import time
import os
import sys
print("Welcome to the temperature converter")
def user_input():
    global temp_input
    global unit_input
    global unit_output 

    temp_input = float(input("Enter the temperature: "))
    unit_input = str(input("""Please choose the unit of temperature from which you want to convert : 
    C
    K
    F
    R
                        
    """))
    unit_output = str(input("Please enter the unit of temperature to which you want to convert : "))

user_input()

#Program termination function

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

#Program continue/exit function
def carry():
    Y_or_N = str(input("Do you want to continue with othe unit conversion? Y/N: "))
    if Y_or_N.casefold() == 'y':
        user_input()
        conversion()
        carry
    else:
        teminate_program()
        
#Functions of Conversion To Kelvin
def cel_to_kel():
    K = temp_input + 273.15
    print(K)

def far_to_kel():
    K = (((temp_input - 32) * 5) / 9) + 273.15
    print(K)

def ran_to_kel():
    K = temp_input/1.8
    print(K)

#Functions of Conversion To Celsius
def kel_to_cel():
    C = temp_input - 273.15
    print(C)

def far_to_cel():
    C = ((temp_input - 32) * 5) / 9
    print(C)

def ran_to_cel():
    C = ((temp_input - 491.67) * 5) / 9
    print(C)

#Functions of conversion To Rankie
def cel_to_ran():
    R = (temp_input + 273.15) * 1.8
    print(R)

def kel_to_ran():
    R = temp_input * 1.8
    print(R)

def far_to_ran():
    R = temp_input + 459.67 
    print(R)

#Functions of conversion to Farenheit
def cel_to_far():
    F =(temp_input * (9/5)) + 32
    print(F)

def kel_to_far():
    F = (((temp_input - 273.15) * 9) / 5) + 32
    print(F)

def ran_to_far():
    F = temp_input - 459.67
    print(F)

     
#Conditions for conversion
def conversion():

    #Conversion from other units to kelvin

    if unit_output.casefold() == 'k':
        if unit_input.casefold() == 'c':
            cel_to_kel()
        elif unit_input.casefold() == 'f':
            far_to_kel()
        elif unit_input.casefold() == 'r':
            ran_to_kel()
        else:
            print("Please enter a valid unit: ")

    #Conversion from other units to celsius

    elif unit_output.casefold() == 'c':   
        if unit_input.casefold() == 'k':
            kel_to_cel()
        elif unit_input.casefold() == 'f':
            far_to_cel()
        elif unit_input.casefold() == 'r':
            ran_to_cel()
        else:
            print("no")

    #Conversion from other units to rankie

    elif unit_output.casefold() == 'r':   
        if unit_input.casefold() == 'c':
            cel_to_ran()
        elif unit_input.casefold() == 'k':
            kel_to_ran()
        elif unit_input.casefold() == 'f':
            far_to_ran()
        else:
            print("no")
       
    #Conversion from other units to farenheit

    elif unit_output.casefold() == 'f':   
        if unit_input.casefold() == 'c':
            cel_to_far()
        elif unit_input.casefold() == 'k':
            kel_to_far()
        elif unit_input.casefold() == 'r':
            ran_to_far()
        else:
            print("no")

    else:
        return 0
    carry()

#Calling conversion() function        
conversion()  