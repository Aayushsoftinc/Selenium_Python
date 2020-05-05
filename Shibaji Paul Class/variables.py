# Names are just references
# Objects are real allocation in computers memory

x = 10 # x -----> object 10
print(type(x))
print(id(x))

y = 12
print(id(y))

y = 10
print(id(y))

# In the following line, declare a variable with name as grade_point and assign 9.5 to grade_point
# In the next line declare a variable with name as age and assign 15 to it.
# in the next line write a print statement that should print - Your age is 15 and your grade point is 9.5.
# Notice the "." at the end and also there should be a new line at the end of line.

grade_point = 9.5
age = 15
print(" Your age is",age, "and your grade point is",grade_point,".","\n")

# Variable Rules:
# Rule 1: cannot use key word as a variable name
#class = "Hello"

#Rule 2: It cannot have space in the variable name
#first name = "Pushkar"

#Rule 3: you cannot have special characters
#first$name = 'Tango'

#Rule 4: variables are case sensitive

#Rule 5: Digit can't be the first character while declaring a variable
#1var =  100

a,b,c = 10,3,9
print(a + b)


