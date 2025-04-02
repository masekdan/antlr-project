import sys
from antlr4 import *
from exprLexer import exprLexer
from exprParser import exprParser
from exprListener import exprListener
from exprVisitor import exprVisitor

class EvalListener(exprListener):
    def __init__(self):
        self.memory = {}

    def enterDeclaration(self, ctx):
        var_type = ctx.primitiveType().getText()
        for i in ctx.IDENTIFIER():
            var_name = i.getText()
            if var_type == "int":
                self.memory[var_name] = 0
            else:
                self.memory[var_name] = 0.0
    
    def enterAssignment(self, ctx):
        var_name = ctx.IDENTIFIER.getText()
        value = self.evaluate(ctx.expr())
        self.memory[var_name] = value
    
    def enterPrintExpr(self, ctx):
        value = ctx.evaluate(ctx.expr())
        print(value)

    def enterInt(self, ctx):
        return int(ctx.getText())


        
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = exprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = exprParser(stream)
    tree = parser.prog()

    #visitor = EvalVisitor()
    #result = visitor.visit(tree)
    #print(result)

if __name__ == '__main__':
    main(sys.argv)