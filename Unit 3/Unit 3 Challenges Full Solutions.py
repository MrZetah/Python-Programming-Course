# Unit 3 Challenge Problems - Full Solutions

#######################################################

# Challenge 1

list_one = [3, 4, 9, 6, 3, 7, 2]

sum = list_one[0] + list_one[-1]   # the -1 index pulls the last item from a list
print(sum)

#######################################################

# Challenge 2

list_one = [3, 4, 9, 6, 3, 7, 2]
total = 0

for number in list_one:
    total += number
print(total)

#######################################################

# Challenge 3

string_list = ['spartan', 'ROCORI', 'Zetah is Awseome!', 'Python Rocks!', 'fun']
length_of_strings = []

for string in string_list:
    length_of_strings.append(len(string))
print(length_of_strings)

#######################################################

# Challenge 4

string_list = ['spartan', 'ROCORI', 'Zetah is Awseome!', 'Python Rocks!', 'fun']
longest_string = ''
longest_length = 0

for string in string_list:
    if len(string) > longest_length:
        longest_length = len(string)
        longest_string = string

print(longest_string)

#######################################################

# Challenge 5

list_one = [3, 4, 9, 6, 3, 7, 2]
list_two = [3, 9, 5, 8, 7, 1]
common_numbers = []

for number in list_one:
    if number in list_two and number not in common_numbers:
        common_numbers.append(number)
        
common_numbers.sort()

print(common_numbers)

