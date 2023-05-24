class Ifstatement:
    def __init__(self,expression,ifStatement,elseStatement):
        self.ifStatement = ifStatement
        self.expression = expression
        self.elseStatement = elseStatement
    def execute(self):
        result = self.expression.eval()
        if result:
            self.ifStatement.execute()
        elif self.elseStatement != None:
            self.elseStatement.execute()


