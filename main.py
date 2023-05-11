from Lexer import *
from Parser import *

def main():
    string_input = "if (3 > 2) loh = 2 + 4"
    obj = Lexer(string_input)
    tokens = obj.Tokinize()
    print(tokens)
    parser = Parser(tokens)
    statement = parser.parse()
    print(variables)
    program = parser.parse()
    # for stmt in program:
    #     if stmt is not None:
    #         stmt.execute()

main()
