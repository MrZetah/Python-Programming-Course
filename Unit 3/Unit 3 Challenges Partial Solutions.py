# Unit 3 Challenge Problems - Partial Solutions

#######################################################

# Challenge 1

list_one = [3, 4, 9, 6, 3, 7, 2]

sum = list_one[__] + list_one[__]   # Fill in the blanks

                # print the sum

#######################################################

# Challenge 2

list_one = [3, 4, 9, 6, 3, 7, 2]
total = 0

for number in list_one:
                # add each number in the list to the total

        # print the total

#######################################################

# Challenge 3

string_list = ['spartan', 'ROCORI', 'Zetah is Awseome!', 'Python Rocks!', 'fun']
length_of_strings = []

for _______ in string_list:             # Fill in the blanks
    length_of_strings.append(__________)  # how do you find the length of each string?   
print(length_of_strings)

#######################################################

# Challenge 4

string_list = ['spartan', 'ROCORI', 'Zetah is Awseome!', 'Python Rocks!', 'fun']
longest_string = ''
longest_length = 0

for string in string_list:
    if len(string) > longest_length:  # If the current string is bigger than any string before....
                        # Set the longest_length variable to the current length 
                        # Set the longest_string variable to the current string

print(longest_string)

#######################################################

# Challenge 5

list_one = [3, 4, 9, 6, 3, 7, 2]
list_two = [3, 9, 5, 8, 7, 1]
common_numbers = ___        # How do you create an empty list??  Fill in the blank

for ________ in ________:  # Loop through the numbers in list_one
    if __________  and __________:          # Two conditions needed. Is the number in list_one also 
        common_numbers.append(number)       #  in list_two, and has it already been added to the common_numbers list?
        
common_numbers.sort()

print(common_numbers)







