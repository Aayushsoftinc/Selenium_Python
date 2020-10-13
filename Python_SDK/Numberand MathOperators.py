num1 = 10
num2 = 2.5
print(type(10))
print(type(2.5))

# Numbers - math operations

print(num1 + num2)
print(5 + 1) # addition
print(5 - 2) # Substraction
print(4 / 2) # Division
print(4 * 2) # Multiplication
print(4 ** 2) # raising to a power
print(5 % 2) # modulo(this means finding out the remainder after division of one number by another)

print(3 / 2) #float division
print(3 // 2) # integer division

# Numbers - Orders of evaluation in math operators
# Highest priority: raising to a power; Medium Priority: division, multiplication and modulo; Low Priority: addition and substraction

print(100 - 5 **2 / 5 *2) # output is 90

print(int(2.5))
print(float(3))
print(max(100, 101))
print(min(25, 30))
print(pow(3, 2))