statements = []

def addStatement(statement):
    statements.append(statement)

def executeStatement():
    for i in range(len(statements)):
        statements[i].execute()