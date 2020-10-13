# from <filename> import <Class name>


from OopsDemo import Calculator


class ChildInheri(Calculator):
    num2 = 400
    def __init__(self):
        Calculator.__init__(self,2,10) # Call parent constructor

    def getCompleteData(self):
        return self.num2 +self.num +self.summation()

obj = ChildInheri()
print(obj.getCompleteData())