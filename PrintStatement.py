class PrintStatement:
    def __init__(self, expression):
        self.expression = expression
    def execute(self):
        print(self.expression.eval())