class BlockStatement:
    statements = []
    # def __init__(self, statement):
    #     self.statements = statement

    def add(self, statement):
        self.statements.append(statement)

    def execute(self):
        for i in range(len(self.statements)):
            self.statements[i].execute()