a = "Hello Pushkar"
b = "Your GPA is 5.0"

print(a+" Congratulations - " +b)

# Playing with List Data Type

values = [4,5, "Pushkar",7.25, "Tamhane"]
print(values)

values[2] = "PUSHKAR"

values.insert(3, "LION KING")
print(values)

values.append("THE END")
print(values)

del values[0]
print(values)

print(values[2:4])

# Playing with the Dictionary Data Type
a = {1: "First_Name", 2: "Second_Name", "age":41}

print(a[1])
print(a["age"])