
# Unit 5 Function Challenge Problems - Partial Solutions

#######################################################

# Challenge 1

def fahrenheit_to_celsius(far):
    celsius = _______________      # Add the necessary calculations
    return round(__________, 2)   # which variable should you return?

celsius = fahrenheit_to_celsius(100)   
print(celsius)

#######################################################

# Challenge 2

def vowel_counter(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ______________:   # What do you need to loop through?
        if ________ in vowels:  # check to see if letter (from the for loop) is in the vowel list
            ______________      # If the letter is a vowel, what do you need to do here?
    return ________         # which variable should you return?
    
print(vowel_counter('How many vowels are in this string'))

#######################################################

# Challenge 3

numbers = [3, 5, 7, 3, 21, 54, 9, 4, 0, 6]

def sum_of_numbers_list(numbers_list):
    total = 0
    for ______________:     # loop through numbers list
        ______________      # Add each number in the list to the total
    return total
    
print(____________________)    # How would you call upon the function properly here?

#######################################################

# Challenge 4

def reverse_string(string):
    _______________________  # There are a few ways to do this. Look up how to take a reverse slice of a string
    return reversed_string
    
example_string = 'Reverse this string'

print(__________________)     # How would you call upon the function properly here?

#######################################################

# Challenge 5

strings = ['hi', 'how are you', 'I am running out of example strings', 'One more should suffice', 'Done']

def find_longest_string(__________):  # add a parameter
    longest_string = ''
    for ___________________ :       # Loop through the list that you passed in through the parameter
        if ______________________:  # Check to see if the length of the current string is longer than the longest stored string
            longest_string = ____________     # If it is, update the longest_string variable to the current string since it is longer
    return ____________   # once the entire loop is finished, return the longest string that was found.
    
print(_______________)
        

#######################################################

# Challenge 6

numbers = [3, 5, 7, 3, 21, 54, 9, 4, 0, 6]

def even_filter(____________):
    even_list = []
    for _______________:
        ____________
        ____________
            
    return even_list
    
print(even_filter(numbers))
