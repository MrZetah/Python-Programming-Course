# Unit 4 Challenge Problems - Partial Solutions

#######################################################

# Challenge 1

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}

                    # There is a method you can call on sets called "intersection". Look up how to use it

#######################################################

# Challenge 2

oldest_age = 0
oldest_person = ''

for name, age in age_dict.items():
    if age > ___________:
        oldest_age = ______________
        oldest_person = ______________

print(f'{_________} is {__________} years old')

#######################################################

# Challenge 3

character_tally = {}

for __________________:     # Loop through characters in string
    character_tally.setdefault(____________)  # look up how to use setdefault method
    character_tally[character] += 1
    
for k, v in character_tally.items():
    print(f'____________')    # print key, value pairs like this -->  a: 5
    
#######################################################

# Challenge 4

total = 0

for ______________________:     # loop through just the values of the grades dictionary
    ______________              # Add each grade to the total
    
average = ______________        # Calculate the average using the total and the length of the dictionary (don't hard code in the number of students)

print(round(average, 2))

#######################################################

# Challenge 5

total = 0

for product in __________________:     # Loop through just the keys of the products dictionary
    total += products_dict[product]['________'] * products_dict[product]['_________']
    
print(f'${round(total, 2)}')
