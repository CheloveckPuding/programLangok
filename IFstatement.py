class Ifstatement:
    def __init__(self,expression,ifStatement):
        self.expression = expression
        self.ifStatement = ifStatement
    def execute(self):
        result = self.expression.eval()
        if result:
            self.ifStatement.execute()

