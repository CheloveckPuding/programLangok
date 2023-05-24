class DoWhileStatement:
    def __init__(self,condition,statement):
        self.condition = condition
        self.statement = statement
    def execute(self):
            while True:
                self.statement.execute()
                if self.condition.eval():
                    continue
                else:
                    break