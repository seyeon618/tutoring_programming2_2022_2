class Calc:
    def __init__(self, operator, num1, num2):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2

    def calc(self):
        if(self.operator == "+"):
            return self.num1 + self.num2
        elif(self.operator == "-"):
            return max(self.num1, self.num2) - min(self.num1, self.num2)
        elif(self.operator == "/"):
            return max(self.num1, self.num2) / min(self.num1, self.num2)
        elif(self.operator == "*"):
            return self.num1 * self.num2
    
operator = input("연산자 입력: ")
num1 = int(input("첫번째 수 입력: "))
num2 = int(input("두번째 수 입력: "))

calc = Calc(operator, num1, num2)
print("result: ", calc.calc())