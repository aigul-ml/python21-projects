class Calc: 
    def __init__(self, color):
        self.color = color 

    def add(self, a, b):
        """Функция сложения """
        return a + b  

    def sub(self, a, b): 
        "Subtraction function"
        return a - b

    def mul(self, a, b): 
        "Multiply function"
        return a * b

    def div(self, a, b): 
        "Division function"
        return a/ b
    
    def true_div(self, a, b): 
        "Division on whole number"
        return a // b

    def mod(self, a, b): 
        "Функция нахождения остатка от деления"
        return a % b
    
    def divmod(self, a, b): 
        "Функция возвращает целое число и остаток от деления"
        return self.true_div(a, b), self.mod(a, b)

    def pow(self, a, b): 
        "Функция возведения числа в степень"
        return a ** b 
    
    def sqrt(self, a, ndigits = 2): 
        "Функция нахождения квадратного корня числа с округлением"
        # return a ** 0.5 
        import math 
        sqrt_num = math.sqrt(a)
        return round(sqrt_num, ndigits)

    def percent(self, total, _percent): 
        "Функция нахождения процента от числа"
        return (total * _percent) / 100

    def __str__(self) -> str:
        return f'{self.color} calculator'

    def super_func(self, string): 
        "Do everything you want"
        return eval(string)

obj1 = Calc('blue')
obj2 = Calc('purple')

obj1.add(4, 5)   # 9 
obj2.add(4, 5)   # 9 
print(obj1)

print(eval(input()))