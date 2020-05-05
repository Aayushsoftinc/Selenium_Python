str = "AayushSoftInc.com"
str1 = " Consulting firm"
str3 = "Aayush"

print(str[1])
print(str[0:6]) # if you want substring in Python
print(str + str1) # Concatenation

print(str3 in str) # Substring check, To check one string is present in another string

# Splitting of string

split = str.split(".")
print(split)

print(split[0])

# Trimming of String

str4 = "  great  "
print(str4.strip())

str5= "  Hello  "
print(str5.lstrip())  # left strip