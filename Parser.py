from NumberExpression import *
from Operations import *
from UnaryExpression import *
from AssigmentStatement import *
from VariableExpression import *
from While_statement import *
from BlockStatement import *
from IFstatement import *
from  DoWhileStatement import *
from PrintStatement import *
from ForStatement import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.size = len(tokens)

    def parse(self):
        result = BlockStatement()
        while(not self.match("EOF")):
            st = self.statement()
            result.add(st)
        return result

    def block(self):
        block = BlockStatement()
        self.pos += 1
        while (not self.match("RBRACE")):
            block.add(self.statement())
        return block

    def statementOrBlock(self):
        if list(self.get(0))[0] == "LBRACE":
            return self.block()
        else:
            return self.statement()

    def statement(self):
        if self.match("FOR"):
            return self.forStatement()
        if self.match("WHILE"):
            return self.WhileStatement()
        if self.match("IF"):
            return self.Ifstatement()
        if self.match("DO"):
            return self.DOWhileStatement()
        if self.match("PRINT"):
            return PrintStatement(self.Expression())
        return self.assigmentStatement()

    def assigmentStatement(self):
        current = self.get(0)
        if (self.match("WORD") and list(self.get(0))[0] == "EQ"):
            variable = current["WORD"]
            self.pos += 1
            resultToVariable = self.Expression()
            result_Variable = AssigmentStatement(variable, resultToVariable)
            result_Variable.execute()
            return result_Variable
        raise Exception("Unknown Statement")

    def forStatement(self):
        if list(self.get(0))[0] == "LPAREN":
            self.pos += 1
            start = self.primary()
            if list(self.get(0))[0] == "COMMA":
                self.pos += 1
                finish = self.primary()
                if list(self.get(0))[0] == "RPAREN":
                    self.pos += 1
                    block = self.statementOrBlock()
                    statement = ForStatement(int(start.eval()), int(finish.eval()), block)
                else:
                    raise Exception("Unknown Statement")
            else:
                raise Exception("Unknown Statement")
        else:
            raise Exception("Unknown Statement")
        return statement

    def WhileStatement(self):
        if list(self.get(0))[0] == "LPAREN":
            self.pos += 1
            condition = self.conditionsOP()
            if list(self.get(0))[0] == "RPAREN":
                self.pos += 1
                block = self.statementOrBlock()
                statement = WhileStatement(condition,block)
                return statement
            else:
                raise Exception("Rparen is left")
        else:
            raise Exception("Lparen is left")

    def Ifstatement(self):
        if list(self.get(0))[0] == "LPAREN":
            self.pos += 1
            expression = self.conditionsOP()
            if list(self.get(0))[0] == "RPAREN":
                self.pos += 1
                block = self.statementOrBlock()
            else:
                raise Exception("Rparen is left")
            if self.match("ELSE"):
                elseStatement = self.statementOrBlock()
            else:
                elseStatement = None
        else:
            raise Exception("Lparen is left")
        statement = Ifstatement(expression,block,elseStatement)
        return statement

    def DOWhileStatement(self):
        block = self.statementOrBlock()
        if self.match("WHILE"):
            self.pos += 1
            condition = self.conditionsOP()
            self.pos += 1
        else:
            raise Exception("While statement is missing")
        statement = DoWhileStatement(condition,block)
        return statement

    def Expression(self):
        return self.additive()

    def additive(self):
        result = self.multiplicative()
        while (True):
            if (self.match("PLUS")):
                result = Operations("+", result, self.multiplicative())
                continue
            if (self.match("MINUS")):
                result = Operations("-", result, self.multiplicative())
                continue
            break

        return result

    def multiplicative(self):
        result = self.unary()

        while(True):
            if(self.match("MULTY")):
                result = Operations("*", result, self.unary())
                continue
            if (self.match("DEL")):
                result = Operations("/", result, self.unary())
                continue
            break

        return result

    def unary(self):
        if (self.match("MINUS")):
            return UnaryExoression("-", self.primary())
        if (self.match("NOT")):
            return UnaryExoression("!", self.primary())
        return self.primary()

    def primary(self):
        current = self.get(0)
        if (self.match("NUMBER")):
            numberExrpession = NumberExpression(float(current["NUMBER"]))
            return numberExrpession
        if(self.match("LPAREN")):
            result = self.Expression()
            self.match("RPAREN")
            return result
        if(self.match("WORD")):
            variablesexpression = VariableExpression(current["WORD"])
            return variablesexpression
        raise Exception('unknown expression')

    def conditionsOP(self):
        result = self.primary()
        while True:
            if (self.match("SMALLEQ")):
                result = Operations("<=", result, self.primary())
                continue
            if (self.match("BIGEQ")):
                result = Operations(">=", result, self.primary())
                continue
            if (self.match("SMALL")):
                result = Operations("<", result, self.primary())
                continue
            if (self.match("BIG")):
                result = Operations(">", result, self.primary())
                continue
            if (self.match("EQUALITY")):
                result = Operations("==", result, self.primary())
                continue
            break
        return result

    def match(self, type):
        current = self.get(0)
        if(type != list(current)[0]):
            return False
        self.pos += 1
        return True

    def get(self, relativePosition):
        position = self.pos + relativePosition
        if(position >= self.size):
            return {"EOF": ""}
        return self.tokens[position]