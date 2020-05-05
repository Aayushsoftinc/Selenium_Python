# In Python,function is a group of related statements that perform a specific task.

#function declaration
#def is an identifier to create function

def GreetMe():
    print(" Good Morning")

#function call
GreetMe()

print("********** PARAMETER FUNCTION ****************")
# parameterized function
def Greet(name):
    print(" Welcome,to Python Learning! , "+name)

Greet("Pushkar Tamhane")

print("********** ADD 2 INTEGERS ****************")

# Function doing sum of two integer numbers

def AddInteger(a,b):
    print(a+b)
AddInteger(2,3)

#using return key word
def AddInteger(a,b):
    return a+b
print(AddInteger(2,3))