class NumberEight:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Add(self):
        return self.a + self.b
    def Sub(self):
        return self.a - self.b
    def Div(self):
        return self.a/self.b
    def Mul(self):
        return self.a*self.b

    def __repr__(self):
        return f'{self.a}, {self.b}'

obj_1 = Integer(3, 5)
print(obj_1)
print(obj_1.Add())
print(obj_1.Sub())
print(obj_1.Div())
print(obj_1.Mul())