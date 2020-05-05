income = float(input(" Enter your income: "))
tax = 0.0

if income < 0.0:
    print("invalid income")
else:
    if income < 10000:
        tax = 0.0
    elif income < 25000:
        tax = income * 0.1
    elif income < 50000:
        tax = income * 0.2
    else:
        tax = income * 0.3
print('Tax is: $',tax)
