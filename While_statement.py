class WhileStatement:
    def __init__(self,condition,statement):
        self.condition = condition
        self.statement = statement
    def executeblock(self):
        while (self.condition.eval() != 0):
            self.statement.executeblock()
