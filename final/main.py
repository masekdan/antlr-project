import sys
from antlr4 import *
from LangLexer import LangLexer
from LangParser import LangParser
from LangVisitor import LangVisitor
from TypeChecker import TypeChecker

def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    lexer = LangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LangParser(tokens)
    tree = parser.program()

    visitor = TypeChecker()
    visitor.visit(tree)

    if parser.getNumberOfSyntaxErrors() == 0:
        if visitor.errors:
            print("ERRORS:")
            for e in visitor.errors:
                print(e)
        else:
            print("OK")

    

if __name__ == "__main__":
    main(sys.argv)