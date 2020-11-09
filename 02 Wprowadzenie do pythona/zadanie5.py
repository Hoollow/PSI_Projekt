class Calculator:
    def init(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


dzialanie = Calculator(5,6)

print(dzialanie.add())
print(dzialanie.difference())
print(dzialanie.multiply())
print(dzialanie.divide())
