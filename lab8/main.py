import sys
from antlr4 import *
from exprLexer import exprLexer
from exprParser import exprParser
from exprListener import exprListener
from exprVisitor import exprVisitor
from antlr4.tree.Tree import ParseTreeWalker

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

    def exitExpr(self, ctx):
        if ctx.getChildCount() == 1:
            if ctx.INT():
                return int(ctx.INT().getText())
            
            elif ctx.FLOAT():
                return float(ctx.FLOAT().getText())
            
            elif ctx.IDENTIFIER():
                var_name = ctx.IDENTIFIER().getText()
                return self.memory.get(var_name, 0)
            
        elif ctx.getChildCount() == 3:
            left = self.evaluate(ctx.expr(0))
            right = self.evaluate(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == '+': return left+right
            if op == '-': return left+right
            if op == '*': return left+right
            if op == '/': return left+right

        return 0

        
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = exprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = exprParser(stream)
    tree = parser.statement()

    listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)