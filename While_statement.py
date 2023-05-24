class WhileStatement:
    def __init__(self,condition,statement):
        self.condition = condition
        self.statement = statement
    def execute(self):
        while self.condition.eval():
            self.statement.execute()
