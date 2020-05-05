'''
Exponent : **
Multiplication: *
Division: /
Floor Division: //
Modulus: %
Substraction: -
'''

# Exponent:
print(2 ** 3)
# Multiplication:
print(3 * 4 * 5) # It's left to right operated - first 3 * 4  12 , later 12 * 5 = 60

#Division
print(15 / 4)
print(type(15/4)) # Gives float input
print(15/3)
print(type(15/3))
print(15 // 4)
print(type(15//4)) # Gives only integer input
print(15//3)

# Modulus - Prints the reminder
print(20%5)
print(23%5)

# Addition
print(15 + 6)
print(12 + 24 + 36) # it's left to right operated - first 12 + 24 = 36, later 36 + 36 = 72

# Substraction
print(15 - 6)
print(36 - 24 - 12) # it's left to right operated - first 36-24 = 12, later 12 - 12 = 0

# Precedence
# First: ** -> Exponent
# Second: * , // ,/ , %
# Third: +, -

print(3 * 6 + 7 - 2/4 ) # first 3*6 = 18 , then added to 7, 18 + 7 = 25, 25 - 0.5 = 24.5
