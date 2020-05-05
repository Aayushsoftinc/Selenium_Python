# Types of String Methods Studied

# index, count, find, lower, upper, startswith, endswith

# Strip, Split and Joint are 3 methods that are frequently used with Strings

# Strings are immutable

str = 'Cisco Switch'
print(str.index("i"))

# To find and print the number of item the alphabets present in a String

print(str.count("i"))

# To print the index location of a substring in a string

print(str.find("Swi"))

print(str.find("xyz"))

# To print string in lower and upper cases
print(str.lower())
print(str.upper())
print(str)

# To print if a string starts and ends with a particular character; Output is in Boolean
print(str.startswith("C"))
print(str.endswith("C"))

# Strip method eliminates all white spaces

b = "     ROCKY HANDSOME     "
print(b.strip())

c= "$$$MONEY MONEY$$$"
print(c.strip("$"))

d = "   Iron Man  "
print(d.replace(" ",""))

# SPLIT method break the strings into sun strings - The result of this method is String

e = "Cisco,Juniper,HP,Avaya,Nortel"
print(e.split(","))

# Joint method
print("_".join(str))

