variables = dict()

def getVariables(key):
    if(not key in variables.keys()):
        raise Exception("variables does not exists")
    return variables[key]

def setVariables(key, value):
    variables[key] = value