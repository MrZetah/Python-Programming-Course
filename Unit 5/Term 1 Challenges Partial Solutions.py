# Term 1 Challenge Problems - Partial Solutions

#######################################################

# Challenge 1

import math

def quadratic_solver(a, b, c):
    try:
        x1 = (-b + math.sqrt(_____________)) / (________)
        x2 = (-b - math.sqrt(_____________)) / (________)
        print(f'____________')

    except ValueError:
        print('There are no real solutions for the values you provided')

a = int(input('Enter the a value for the quadratic equation: '))
b = int(input('Enter the b value for the quadratic equation: '))
c = int(input('Enter the c value for the quadratic equation: '))

______________ # Call on the function with the appropriate arguments

#######################################################

# Challenge 2

def collatz(number):
    while number > 1:
        if ____________:
            # Call on even number function
        else:
            # Call on odd number function.... don't forget to store returned value
        
        print(number)
        
def handle_even_number(number):
    return number // 2
    
def handle_odd_number(number):
    return number * 3 + 1
    
collatz(9)


#######################################################

# Challenge 3

number_list = [1, 3, 4, 9, 23, 65, 93]

def add_numbers_in_list(numbers):
    total = 0 
    #  Use a for loop to loop through the numbers in the list above and add each to the total
    
    return total

print(add_numbers_in_list(number_list))

#######################################################

# Challenge 4

from datetime import datetime

wait_list = {}

def add_to_wait_list(wait_list):
    while True:
        response = input("Type 'y' to add a name or 'n' to stop: ")
        if response == 'y':
            name = input('Enter a name: ')
            date = input('Enter a date (MM/DD/YY): ')
            date_object = datetime.strptime(date, "%m/%d/%y")
            wait_list[name] = date_object
        elif response == 'n':
            return wait_list
        else:
            print('not a valid input')
            
def next_in_line(wait_list):
    most_recent_date = None
    most_recent_name = None

    for name, date in wait_list.items():
        if most_recent_date is None or date > most_recent_date:
            most_recent_date = date
            most_recent_name = name

    return most_recent_name

            
wait_list = add_to_wait_list(wait_list)
print(next_in_line(wait_list))

#######################################################

# Challenge 5

def encrypt(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message=''
    for letter in message:
        letter = letter.lower()
        if letter in alphabet:
            # encrypt the character if it is a letter
            ____________________        # Find the index of your letter in the alphabet
            ____________________        # Add 5 to the index value, but use remainder 26 incase value goes above 26 
            encrypted_message = encrypted_message + new_letter
        else:
            # If character is not a letter, just add it to the encrypted message without encrypting it
            encrypted_message = encrypted_message + letter
    
    return encrypted_message
    
print(encrypt('Encrypt this M3ssage'))

#######################################################

# Challenge 6

def retirement_calculator(start_age, retire_age, annual_contributions, interest):
    total_money = 0
    for year in range(start_age, retire_age):
        _________________    # Multiply the amount in total money by the interest rate (don't forget to add 1 to it)
        _________________    # Add the annual contribution to the total
    
    return total_money
    
print(retirement_calculator(20, 60, 5000, 0.07))    # You should get 998 million if you set up the function right and run it with these arguments







