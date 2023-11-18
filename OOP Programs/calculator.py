class Calculator:
    def add(self,a,b):
        self.add=a+b
        return self.add
    def sub(self,a,b):
        self.sub=a-b
        return self.sub
    def mul(self,a,b):
        self.mul=a+b
        print("Multiplication : ",self.mul)
#Above Class Creation is Known as Blueprint of object


#Here calc is object of Class Calculator
calc=Calculator()

x=calc.add(3,4)
print("sum is : ",x)

y=calc.sub(10,4)
print("sum is : ",y)