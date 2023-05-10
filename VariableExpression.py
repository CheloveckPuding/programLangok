from Variables import *

class VariableExpression:
    def __init__(self, name):
        self.name = name


    def eval(self):
        return getVariables(self.name)