drawing_list = ['''
            ----
           |    |
           |
           |
           |
           |
           |
          =========''',
          '''
            ----
           |    |
           |    O
           |
           |
           |
           |
          =========''',
          '''
            ----
           |    |
           |    O
           |    |
           |    |
           |
           |
          =========''',
          '''
            ----
           |    |
           |    O
           |    |
           |    |
           |     \\
           |
          =========''',
          '''
            ----
           |    |
           |    O
           |    |
           |    |
           |   / \\
           |
          =========''',
          '''
            ----
           |    |
           |    O
           |    |/
           |    |
           |   / \\
           |
          =========''',
          '''
            ----
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
           |
          =========''']

answer = 'type an answer here'   # change this string
count = 0
correct_guesses = []
wrong_guesses = []

print(drawing_list[count])
for i in answer:
    if i.isalpha():
        print('_', end='')
    elif i.isdigit():
        print('_', end='')
    else:
        print(' ', end='')
print()
guess = input('Guess a letter: ')

while count < 5:
    if guess not in answer:
        print('Incorrect guess!')
        count += 1
        wrong_guesses.append(guess)
        print(drawing_list[count])
        for i in answer:
            if i in correct_guesses:
                print(i, end='')
            elif i.isalpha():
                print('_', end='')
            elif i.isdigit():
                print('_', end='')
            else:
                print(' ', end='')
        print()
        print('Wrong Guesses: ',wrong_guesses)
        guess = input('Guess another letter: ')

    else:
        print('Nice Guess!')
        correct_guesses.append(guess)
        print(drawing_list[count])
        for i in answer:
            if i in correct_guesses:
                print(i, end='')
            elif i.isalpha():
                print('_', end='')
            elif i.isdigit():
                print('_', end='')
            else:
                print(' ', end='')
        print()
        print('Wrong Guesses: ',wrong_guesses)
        guess = input('Guess another letter: ')

count += 1
print(drawing_list[count])
print('You Lose!!!!')
