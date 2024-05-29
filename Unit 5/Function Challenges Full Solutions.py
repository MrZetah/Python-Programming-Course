
# Unit 5 Function Challenge Problems - Full Solutions

#######################################################

# Challenge 1

def fahrenheit_to_celsius(far):
    celsius = (far - 32) * 5/9
    return round(celsius, 2)

celsius = fahrenheit_to_celsius(100)   
print(celsius)

#######################################################

# Challenge 2

def vowel_counter(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count
    
print(vowel_counter('How many vowels are in this string'))

#######################################################

# Challenge 3

numbers = [3, 5, 7, 3, 21, 54, 9, 4, 0, 6]

def sum_of_numbers_list(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total
    
print(sum_of_numbers_list(numbers))

#######################################################

# Challenge 4

def reverse_string(string):
    reversed_string = string[::-1]  # This is how you take a backwards slice of an entire list or string
    return reversed_string
    
example_string = 'Reverse this string'

print(reverse_string(example_string))

#######################################################

# Challenge 5

strings = ['hi', 'how are you', 'I am running out of example strings', 'One more should suffice', 'Done']

def find_longest_string(list_of_strings):
    longest_string = ''
    for string in list_of_strings:
        if len(string) > len(longest_string):  # Is the current string longer than the longest stored string
            longest_string = string     # If it is, update the longest_string variable to the current string since it is longer
    return longest_string   # once the entire loop is finished, return the longest string that was found.
    
print(find_longest_string(strings))
        

#######################################################

# Challenge 6

numbers = [3, 5, 7, 3, 21, 54, 9, 4, 0, 6]

def even_filter(numbers_list):
    even_list = []
    for number in numbers_list:
        if number % 2 == 0:
            even_list.append(number)
            
    return even_list
    
print(even_filter(numbers))
