class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

#Ushbu joyda biz limit kiritib qo'yishimniz kerak
limit = 400
fibonacci_iter = FibonacciIterator(limit)
for num in fibonacci_iter:
    print(num)
