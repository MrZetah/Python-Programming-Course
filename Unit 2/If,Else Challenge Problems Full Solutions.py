# If/Else Challenge Problems - Full Solutions

#######################################################

# Challenge 1
number = int(input('Enter a number '))

if number % 2 ==0:
    print(number, 'is even')
else:
    print(number, 'is odd')

#######################################################

# Challenge 2
password = 'zetah is awesome'
guess = input('Enter the Password: ')

if guess == password:
    print('Access Granted')
else:
    print('Access Denied')

#######################################################

# Challenge 3
number = int(input('Enter a Number '))

if number > 0:
    print(number, 'is positive')
elif number < 0:
    print(number, 'is negative')
else:
    print(number, 'is 0')

#######################################################

# Challenge 4
number = int(input('Enter a Number: '))

if number % 3 == 0 and number % 5 == 0:
    print(number, 'is a multiple of 3 and 5')
elif number % 3 == 0:
    print(number, 'is a multiple of 3')
elif number % 5 == 0:
    print(number, 'is a multiple of 5')
else:
    print(number, 'is not a multiple of 3 and 5')


#######################################################

# Challenge 5
grade = int(input('What is your grade? '))

if grade > 90:
    print('You got an A! Great Job!')
elif grade > 80:
    print('You got a B, Nice!')
elif grade > 70:
    print('You got a C!')
elif grade > 60:
    print('You got a D, phew')
else:
    print('You got an F, better study.')



#######################################################

# Challenge 6

x = int(input('Enter a numebr: '))
y = int(input('Enter a second numebr: '))
z = int(input('Enter a third numebr: '))

if x > y > z:
    print(x, 'is the largest, and' ,z, 'is the smallest')

elif x > z > y:
    print(x, 'is the largest, and' ,y, 'is the smallest')
    
elif y > x > z:
    print(y, 'is the largest, and' ,z, 'is the smallest')
    
elif y > z > x:
    print(y, 'is the largest, and' ,x, 'is the smallest')
    
elif z > x > y:
    print(z, 'is the largest, and' ,y, 'is the smallest')
    
elif z > y > x:
    print(z, 'is the largest, and' ,x, 'is the smallest')
    
    
    
    
    
    

