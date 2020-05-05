x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

# max = 0
# if x > y:
#    max = x
#else:
#    max = y

max = x if x > y else y

print('Maximum is: ',max)

print("***********************************************************************************")

# elif code
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

# max = 0
# if x > y:
#    max = x
#else:
#    max = y

max = a if a > b  and a > c else b if b > c else c

print('Maximum is: ',max)