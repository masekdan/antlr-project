import sys
from antlr4 import *
from LangLexer import LangLexer
from LangParser import LangParser
from TypeChecker import TypeChecker  # náš listener

def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    lexer = LangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LangParser(tokens)
    tree = parser.program()

    walker = ParseTreeWalker()
    checker = TypeChecker()
    walker.walk(checker, tree)

    if checker.errors:
        print("\n".join(checker.errors))
    else:
        print("OK!")

if __name__ == "__main__":
    main(sys.argv)