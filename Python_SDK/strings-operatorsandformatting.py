a = 'Costco'
b = "Warehouse"
c = a + b

print(c)
print(a * 3)

print("t" in a)
print("z" in a)

print("z" not in a)

# For Dynamic change we use the % Operator with %s for string, %d for digit and %f for floating numbers

print(" Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM",2, 12.4))

# for floating numbers to return only one number after decimal
print(" Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM",2, 12.4))
# for floating numbers to return only 2 number after decimal
print(" Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM",2, 12.4))

# for floating numbers to return no decimal
print(" Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM",2, 12.4))

# Another format using curly braces and format method
print(" Cisco model: {}, {} WAN slots, IOS {}".format ("2600XM",2, 12.4))

print(" Cisco model: {0}, {1} WAN slots, IOS {2}".format ("2600XM",2, 12.4))

print(" Cisco model: {2}, {0} WAN slots, IOS {1}".format ("2600XM",2, 12.4))