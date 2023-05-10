class UnaryExoression:
    def __init__(self, operation, expr1):
        self.operation = operation
        self.expr1 = expr1

    def eval(self):
        if (self.operation == "-"):
            return -self.expr1.eval()
        if(self.operation == "!"):
            line = bin(self.expr1.eval())[2::]
            newline = ''
            for i in range(len(line)):
                if(line[i] == '1'):
                    newline += '0'
                else:
                    newline += '1'
            return int(newline, 2)

