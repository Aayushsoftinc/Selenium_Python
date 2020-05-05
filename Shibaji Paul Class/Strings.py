s1 = "This is Ela's Birthday!!"
print(s1)
# To calculate character length in Strings

print(len(s1))

p1 = '50' # This is string variable
print(type(p1))

x = int(p1)
print(x)
print(type(x))

s2 = '6.5'
f = float(s2)
print(f)
print(type(f))

# Stripping the String
z1 = '   Rocky  '
#print(len(z1))
z2 = z1.strip()
print(len(z2))

# Convert binary,octal or hex strings
# Step 1: Binary string conversion
b1 = '1100'
b2 = int(b1,2) # 2 passed as base second parameter
print(b2)
# Step 2: Hexadecimal string conversion
b3 = '1a'
b4 = int(b3,16) # 16 passed as base second parameter
print(b4)

# Step 2: Octal string conversion
b5 = '1001010'
b6 = int(b5,8) # 8 passed as base second parameter
print(b6)