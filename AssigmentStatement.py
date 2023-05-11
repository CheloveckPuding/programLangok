from Variables import *

class AssigmentStatement:
    def __init__ (self, variable, result):
        self.variable = variable
        self.result = result

    def executeblock(self):
        setVariables(self.variable, self.result.eval())


