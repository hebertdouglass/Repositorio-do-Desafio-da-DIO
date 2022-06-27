class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.div())
    print(calculadora.mult())


    # print(soma(1, 2))
    # print(soma(10, 2))
    # print(sub(10, 2))
    # print(mult(10, 2))
    # print(div(10, 2))