from Lexer import *
from Parser import *

def main():
    string_input = open("Test.txt" , encoding='utf-8').read()
    print(string_input)
    obj = Lexer(string_input)
    tokens = obj.Tokinize()
    print(tokens)
    parser = Parser(tokens)
    statement = parser.parse()
    statement.execute()

main()

# string_input = "ok = 0 do { ok = ok + 3 print ok } while ( ok < 0 ) nice = 0 while ( nice < 0 )  { nice = nice + 3 } "
# string_input = "ok = 1 while ( ok < 3 ) { ok = ok + 1 print ok }"