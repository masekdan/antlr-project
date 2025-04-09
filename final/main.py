import sys
from antlr4 import *
from LangLexer import LangLexer
from LangParser import LangParser
from LangVisitor import LangVisitor
from TypeChecker import TypeChecker
from InstructionGenerator import InstructionGenerator
from VirtualMachine import VirtualMachine

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
            file = open("ot.txt","w")
            generator = InstructionGenerator(visitor.symbol_table,file)
            generator.visit(tree)
            file.close()

            file1 = open("ot.txt","r")
            machine = VirtualMachine(file1)
            machine.eval()
            file1.close()

if __name__ == "__main__":
    main(sys.argv)