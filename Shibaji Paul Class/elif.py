# Write a Program to compare maximum of three numbers
# If X > y and Z then X is max else
# Y or Z is max

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

max = 0
if x > y and x > z:
    print('You are in the If Block')
    max = x
elif y > z:
    print ('You are in the elif block')
    max = y

else:
    print('You are in the else block')
    max = z
print('Maximum is: ',max)
print('Thank, You!!!')