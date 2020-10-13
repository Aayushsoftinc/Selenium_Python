# Classes are user defined blueprint or prototype
#classes have methods, variables, instance variable, constructor etc
# self keyword is mandatory for calling variable names into method

#Constructor is one method which is automatically called when you create object for any class

#Define the classes
class Calculator: # Syntax to define class
    num = 100 # define variable in class - This a class variable and does not change
    # default constructor
    def __init__(self,a,b): #init is keyword to define constructor
        self.firstNumber= a # This is a instance variable
        self.secondNumber= b # This is a  instance variable
        print("I'm called automatically when object is created")

    def getData(self): # Define method in class
        print("Executing method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

# creating object  of class in Python
obj = Calculator(2,3) # create objects in Python
obj.getData()
print(obj.summation())

obj1 = Calculator(4,5) # create objects in Python
obj1.getData()
print(obj1.summation())