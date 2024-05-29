# Unit 4 Dictionary Challenge Problems - Full Solutions

#######################################################

# Challenge 1

example_dictionary = {'first name': 'Jacob', 'last name': 'Zetah', 'occupation': 'teacher', 'characteristic': 'awesome'}
reversed_dictionary = {}

for k, v in example_dictionary.items():
    ___________________    # Set the key and the value in the reversed orientation from how you pulled them from the example dictionary
    
print(reversed_dictionary)

#######################################################

# Challenge 2

string = 'Count how many of each character are in this string. Convert all characters to lowercase so lowercase and uppercase letters are counted separately'
character_count = {}

for character in string:
    character = character._______  # convert all characters to lowercase. Look up the method needed to convert characters to lowercase
    character_count._____________  # if character isn't in dictionary yet add it, but set its value to 0. Look up how to use setdefault method
    character_count[character] += 1    # Add one to the character that is already in the dictionary
    
for k, v in character_count.items():
    print(f'_________')  # print the keys and values of the character count dictionary

#######################################################

# Challenge 3

player_1 = {'sword': 1, 'bow': 1, 'arrows': 5, 'healing potion': 2, 'gold coins': 9}
player_2 = {'dagger': 1, 'healing potion': 4, 'gold coins': 5, 'silver coins': 3}

combined_inventory = {}

for key in _______________:     # loop through the keys of player 1
    if key in player_2.keys():  # If the key is in player two, that means both players have the same item
        combined_inventory[key] = _______________________    # Add the values of the quantity for the similar item from both players
    else:
        combined_inventory[key] = ________________     # If an item only exists in player 1, just add it to the combined dictionary without doing anything to it.
        
for key in player_2.keys():     # loop through the keys of player 2
    if key not in combined_inventory:   # Check to see if there are any items in player 2 that haven't been added to the combined dictionary yet
        ___________________________  # Add player 2 remaining items to combined dictionary 

print(combined_inventory)

