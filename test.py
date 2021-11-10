
class Test:


    def __init__(self, limit):
        self.limit = limit
        self.ant = 0
        self.prox = 1
        self.cont = 0

    def __iter__(self):
        self.x = self.limit
        return self

    def __next__(self):
        x = self.x
        ant = self.ant
        if x < 0:
            raise StopIteration
        else:
            self.x = x - 1
            self.cont = self.ant
            self.ant = self.prox
            self.prox = self.cont + self.ant
        return ant


def Fibo(x):
    Fibo = iter(Test(x))
    dic1 = ({a:b for a,b in enumerate(Fibo)})
    return dic1

print(Fibo(10))
