from Lexer import *
from Parser import *

def main():
    string_input = "while ( 2 > 0 ) { ok = 4 } "
    obj = Lexer(string_input)
    tokens = obj.Tokinize()
    print(tokens)
    parser = Parser(tokens)
    statement = parser.parse()
    print(variables)

main()
