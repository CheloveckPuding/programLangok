class Operations:
    def __init__(self, operation, expr1, expr2):
        self.operation = operation
        self.expr1 = expr1
        self.expr2 = expr2


    def eval(self):
        if (self.operation == "+"):
            return self.expr1.eval() + self.expr2.eval()
        elif (self.operation == "*"):
            return self.expr1.eval() * self.expr2.eval()
        elif (self.operation == "/"):
            return self.expr1.eval() / self.expr2.eval()
        elif (self.operation == "-"):
            return self.expr1.eval() - self.expr2.eval()
        elif (self.operation == '<='):
            return self.expr1.eval() <= self.expr2.eval()
        elif (self.operation == '>='):
            return self.expr1.eval() >= self.expr2.eval()
        elif self.operation == '<':
            return self.expr1.eval() < self.expr2.eval()
        elif self.operation == '>':
            return self.expr1.eval() > self.expr2.eval()
        elif self.operation == '==':
            return self.expr1.eval() == self.expr2.eval()




