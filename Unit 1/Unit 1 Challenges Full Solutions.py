# Unit 1 Challenge Problems - Full Solutions

#######################################################

# Challenge 1
x = int(input("Enter a number and I will square it: "))

squared = x**2

print(f'{x} squared is: {squared}')

#######################################################

# Challenge 2

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

total = x + y

print(f'{x} + {y} = {total}')

#######################################################

# Challenge 3

tax_rate = 0.06875

price = float(input('What is the price of your item? '))
quant = float(input('How many items did you purchase? '))

cost_before_tax = price * quant
taxes = cost_before_tax * tax_rate
total_cost = cost_before_tax + taxes

print(f'Cost before taxes: ${round(cost_before_tax, 2)}')
print(f'Cost of taxes: ${round(taxes, 2)}')
print(f'Total cost, including taxes: ${round(total_cost, 2)}')

#######################################################

# Challenge 4

'''
Create your own challenge and solve it
Ideas:
Enter length of cube side, calculate volume or surface area of cube.
Do same thing with reacangle, but include inputs for length, width, and height

Input radius of a sphere, calculate volume

More advanced option: Create a quadratic equation solver
'''


















