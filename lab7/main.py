import sys
from antlr4 import *
from exprLexer import exprLexer
from exprParser import exprParser
from exprVisitor import exprVisitor

class EvalVisitor(exprVisitor):
    def __init__(self):
        self.memory = {}

    def visitProg(self, ctx):
        results = [self.visit(child) for child in ctx.getChildren() if child.getText() != ';']
        return results
    
    def visitPar(self, ctx):
        return self.visit(ctx.expr())
    
    def visitInteger(self, ctx):
        return int(ctx.getText())
    
    def visitOctal(self, ctx):
        return int(ctx.getText(), base=8)
    
    def visitHexa(self, ctx):
        return int(ctx.getText(), 16)
    
    def visitAdd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == '+':
            return left + right
        else:
            return left - right
        
    def visitMul(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == '*':
            return left * right
        else:
            return left / right
        
        

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = exprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = exprParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print(result)

if __name__ == '__main__':
    main(sys.argv)