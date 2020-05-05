# Open the text file and read the content from test.txt

file = open('test.txt')
# Read the contents of file
# print(file.read())

# To read first number of characters by passing parameter from test.txt file
# print(file.read(2))

# To read line from file
#print(file.readline())
#print(file.readline())
#print(file.readline())


# Method 2: Print line by line using readline method
#line1 = file.readline()
#while line1!="":
#    print(line1)
#    line1 = file.readline()

## Method 3: Print using readlines method
for line in file.readlines():
    print(line)

file.close()