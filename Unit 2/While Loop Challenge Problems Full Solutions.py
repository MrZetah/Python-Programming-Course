# While Loop Challenge Problems - Full Solutions

#######################################################

# Challenge 1
word = input('Enter a word or phrase: ')
num = int(input('How many times would you like it repeated? '))

while num > 0:
    print(word)
    num -= 1

#######################################################

# Challenge 2
number = int(input('Enter a positive whole number: '))
repeat = number - 1

while repeat > 1:
    number = number*repeat
    repeat -= 1
print(number)


#######################################################

# Challenge 3
number = int(input('Enter a number: '))
value = 0

while number > value:
    print(value)
    value += 2

#######################################################

# Challenge 4
total = 0
number = float(input('Enter a number: '))

total += number

while True:
    repeat = input('Enter another number to add to the total, or enter "stop" ')
    if repeat == 'stop':
        print('Your total is' ,float(total))
        break
    else:
        total += float(repeat)


