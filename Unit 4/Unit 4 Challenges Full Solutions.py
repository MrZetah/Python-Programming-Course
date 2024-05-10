# Unit 4 Challenge Problems - Full Solutions

#######################################################

# Challenge 1

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}

print(set_1.intersection(set_2))

#######################################################

# Challenge 2

oldest_age = 0
oldest_person = ''

for name, age in age_dict.items():
    if age > oldest_age:
        oldest_age = age
        oldest_person = name

print(f'{oldest_person} is {oldest_age} years old')

#######################################################

# Challenge 3

character_tally = {}

for character in analyze_this_string:
    character_tally.setdefault(character, 0)
    character_tally[character] += 1
    
for k, v in character_tally.items():
    print(f'{k}: {v}')
    
#######################################################

# Challenge 4

total = 0

for grade in grades_dict.values():
    total += grade
    
average = total / len(grades_dict)

print(round(average, 2))

#######################################################

# Challenge 5

total = 0

for product in products_dict.keys():
    total += products_dict[product]['price'] * products_dict[product]['quant']
    
print(f'${round(total, 2)}')
