
class Calculator:
    def __init__(self, num):
        self.__num = num
           
    def add(self, num):
        self.__num += num
        return self
        
    def subtract(self,num):
        self.__num -= num
        return self
    
    def divide(self,num):
        self.__num /= num
        return self
    
    def multiply(self,num):
        self.__num *= num
        return self
        
    def end(self):
        return self.__num
    
# 강사    
class CalculatorAns:
    def __init__(self, val):
        self.val = val
    
    def add(self, val):
        self.val += val 
        return self
    
    def subtract(self, val):
        self.val -= val
        return self
    
    def divide(self,val):
        self.val /= val
        return self
    
    def multiply(self, val):
        self.val *= val
        return self
    
    def end(self):
        return self.val
        
val = Calculator(10).add(10).add(10).subtract(5).divide(3).end()
print('(10 + 10 + 10 - 5) / 3 = ',val)
# (10 + 10 + 10 - 5)/3 = 8.33333