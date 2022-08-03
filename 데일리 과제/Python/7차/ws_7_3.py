class Calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def substract(self):
        return self.num1 - self.num2

    def multply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다.'


a = Calculator(1, 2)
print(a.add())
b = Calculator(2, 1)
print(b.substract())
c = Calculator(3, 4)
print(c.multply())
d = Calculator(4, 0)
print(d.divide())