# To branch between the section of code based on the condition -> condition based evaluation

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

max = 0
if x > y:
    print('You are in the If Block')
    max = x
else:
    print('You are in the else block')
    max = y
print('Maximum is: ',max)
print('Thank, You!!!')
