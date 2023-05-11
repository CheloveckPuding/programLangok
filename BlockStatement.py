class BlockStatement:
    def __init__(self):
        self.statements = []

    def add(self, statement):
        self.statements.append(statement)

    def execute(self):
        for stmt in self.statements:
            stmt.execute()